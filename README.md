# Professional Profile

An AI assistant interviews you, and together you build a CV (a resume in the US), the text of your LinkedIn profile and a short professional bio, aimed at a specific reader you choose. It writes in English for the UK, US and European markets.

It was designed on research conducted in August and September 2026.

## What you end up with

You choose which of these you want:

- **A CV or resume**, written for one named reader rather than for everyone.
- **LinkedIn text**, for your headline, your About section and your roles.
- **A short bio**, the third-person paragraph that gets circulated when someone introduces you. If you are going for board or advisory work, you will be asked for one of these more often than you expect.

## Before you start, gather these

- **Your current CV.** If you have older versions, bring those too. The assistant reads across them to see what you emphasise when the audience changes.
- **Five to ten pieces of your own writing.** Emails you have sent, a paper, a report, a talk, a LinkedIn post. This is how the assistant learns to write in your voice rather than in its own. You can skip this, and if you do, the LinkedIn text will sound more generic.
- **A real job advertisement or role specification** for the kind of role you want. Not a made-up one. The assistant works from the actual words in it.

## How long it takes

Expect two to three sittings of about an hour, rather than one long session. The process stops and asks you to confirm at seven to nine points, so you can put it down at any of them and come back.

At every stopping point the assistant updates a working record of what you have decided. Keep it. Pasting it into a new conversation is all it takes to carry on, even if a conversation grows too long or you hit your plan's usage limit.

## Two ways to use it

**As a skill, on Claude.** Download `professional-profile.zip` from the latest release. In Claude, check that code execution is on (on Free, Pro and Max plans: Settings, then Capabilities, then "Code execution and file creation"). Then go to Customize, then Skills, click "+", choose "Create skill" and then "Upload a skill". After that, start a conversation and say you want to work on your CV or LinkedIn profile. On a Team or Enterprise plan, your administrator controls whether skills can be used.

**As a pasted prompt, on any assistant.** Download `professional-profile-prompt.txt` from the latest release. Paste the whole file into the instructions of a project (see below), or straight into a new chat, then type "Follow these instructions. Let's begin."

## A word about your information

You are about to paste your real career history into an AI assistant. That is the only way this works, because a CV built from vague information is a vague CV. So this is about choosing knowingly rather than leaving things out.

**If you are job hunting quietly, use a personal account, not your work one.** On a work or school account, your employer's administrator controls the privacy settings and can decide how long your chats are kept. You may not be able to change that, or even see it.

**Each assistant has one setting worth checking**, which controls whether your chats are used to train the AI. You can turn it off before you start.

| Assistant | Where to look |
|---|---|
| Claude | Settings, then Privacy |
| ChatGPT | Settings, then Data Controls, then "Improve the model for everyone" |
| Gemini | Open Activity from the main screen |

One warning about private or temporary chat modes: in Gemini you cannot upload files in a temporary chat, so it will not work for this. Use a normal chat.

You should still leave out anything you would never want stored: your home address, your date of birth, client names you are under an agreement not to mention, and salary figures. None of those improve the documents.

## Set up a project first

All three assistants let you create a container that holds your files and remembers what you are working on across several sittings. Use it. Without one, you are re-explaining yourself every time.

| Assistant | What it is called | Note |
|---|---|---|
| Claude | Projects, or Cowork projects | A new Cowork project is saved to your account and follows you to other devices. One created from a folder on your computer stays on that computer |
| ChatGPT | Projects | Available on the free plan, with up to five files per project |
| Gemini | Gems, or Notebooks | Notebooks are unavailable on work and school accounts |

Put your CV, your writing samples and the job advertisement into the project before you begin.

## One last thing

This is an AI. It is good at structure, at asking the questions you would not think to ask yourself, and at drafting quickly. It is capable of producing something confident and wrong.

Everything it writes is going out under your name, so read it properly before you use it. If a line does not sound like you, say so and ask for it again. If a claim is not one you could defend in an interview, cut it. The assistant is told to expect this and to do what you ask.

## Versions

Every release is kept on the Releases page, so an earlier version is always there if you need it. Settings paths and plan details above were checked on 24 September 2026, apart from the Claude privacy path and the Gemini rows, which were checked on 17 August 2026. Assistants change their menus often, so if something has moved, look for the nearest equivalent.

## Licence

Made by Coeur de Lion. Licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/): you can use, share and adapt it for any non-commercial purpose, as long as you credit Coeur de Lion and say what you changed. The full terms are in [LICENSE](LICENSE).
