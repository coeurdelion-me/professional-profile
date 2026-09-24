#!/usr/bin/env python3
"""Build the two release files from skill/professional-profile/, and check them.

  dist/professional-profile.zip         the skill, for assistants that install skills
  dist/professional-profile-prompt.txt  one self-contained block, for pasting anywhere

The skill folder is the only source. The paste version is generated from it and never
edited by hand. Run from the repository root:  python3 tools/build.py
"""
import os, re, sys, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "skill", "professional-profile")
DIST = os.path.join(ROOT, "dist")

# Reference order in the paste version follows the order the process reaches them.
ORDER = ["locale-uk", "locale-us", "locale-eu", "track-c", "cv", "voice", "writing",
         "ai-tells", "personas", "bio", "linkedin", "qa", "platform-facts"]

failures = []


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        failures.append("SKILL.md has no frontmatter")
        return {}, text
    fm = {}
    for line in m.group(1).split("\n"):
        if re.match(r"^[a-z-]+:", line):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, text[m.end():]


def check_frontmatter(fm):
    allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    for k in fm:
        if k not in allowed:
            failures.append(f"frontmatter field not in the portable spec: {k}")
    name = fm.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        failures.append(f"invalid name: {name!r}")
    if name != os.path.basename(SKILL):
        failures.append("name does not match the folder name")
    d = fm.get("description", "")
    if not d or len(d) > 1024 or "<" in d or ">" in d:
        failures.append(f"description missing, over 1024 characters or has angle brackets ({len(d)})")
    c = fm.get("compatibility", "")
    if len(c) > 500:
        failures.append("compatibility over 500 characters")


def paste_version(body, refs):
    def to_section(m):
        return f'the "Reference: {m.group(1)}" section below'
    out = re.sub(r"`references/([a-z-]+)\.md`", to_section, body)
    for name, text in refs:
        text = re.sub(r"`references/([a-z-]+)\.md`", lambda m: f'the "Reference: {m.group(1)}" section', text)
        text = re.sub(r"^# ", "## ", text, count=1, flags=re.M)
        out += f"\n\n---\n\n# Reference: {name}\n\n" + text.split("\n", 1)[1].lstrip()
    return out.rstrip() + "\n\nFollow these instructions. Let's begin.\n"


def check_text(label, text):
    bad = [c for c in set(text) if ord(c) > 126 or (ord(c) < 32 and c not in "\n")]
    if bad:
        failures.append(f"{label}: non-ASCII or control characters {sorted(bad)!r}")
    for m in re.finditer(r"`references/([a-z-]+)\.md`", text):
        if not os.path.exists(os.path.join(SKILL, "references", m.group(1) + ".md")):
            failures.append(f"{label}: points at a missing file references/{m.group(1)}.md")


def words(text):
    return len(text.split())


def main():
    skill_md = read(os.path.join(SKILL, "SKILL.md"))
    fm, body = split_frontmatter(skill_md)
    check_frontmatter(fm)
    check_text("SKILL.md", skill_md)

    present = sorted(f[:-3] for f in os.listdir(os.path.join(SKILL, "references")) if f.endswith(".md"))
    if sorted(ORDER) != present:
        failures.append(f"reference files and ORDER differ: {sorted(set(present) ^ set(ORDER))}")
    refs = []
    for name in ORDER:
        p = os.path.join(SKILL, "references", name + ".md")
        if os.path.exists(p):
            t = read(p)
            check_text(f"references/{name}.md", t)
            refs.append((name, t))
        if f"`references/{name}.md`" not in skill_md:
            failures.append(f"SKILL.md never names references/{name}.md, so it would never be read")

    prompt = paste_version(body, refs)
    check_text("paste version", prompt)

    print(f"SKILL.md body: {words(body):,} words (always loaded)")
    for name, t in refs:
        print(f"  references/{name}.md: {words(t):,}")
    print(f"skill total: {words(body) + sum(words(t) for _, t in refs):,} words")
    print(f"paste version: {words(prompt):,} words, {len(prompt):,} characters")

    if failures:
        print("\nFAILED:")
        for f in failures:
            print("  - " + f)
        sys.exit(1)

    os.makedirs(DIST, exist_ok=True)
    with open(os.path.join(DIST, "professional-profile-prompt.txt"), "w", encoding="ascii", newline="\n") as f:
        f.write(prompt)
    with zipfile.ZipFile(os.path.join(DIST, "professional-profile.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, _, filenames in os.walk(SKILL):
            for fn in sorted(filenames):
                full = os.path.join(dirpath, fn)
                z.write(full, os.path.relpath(full, os.path.dirname(SKILL)))
    print("\nall checks passed; wrote dist/professional-profile-prompt.txt and dist/professional-profile.zip")


if __name__ == "__main__":
    main()
