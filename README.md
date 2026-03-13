# TeraCreators Help

A community-sourced help guide for TeraCreators games, built from compiled Discord messages, then curated, cleaned, classified, categorized, consolidated, clarified, cross-checked, and converted into practical help for players.

This project is made by someone who genuinely enjoys playing these games and wanted to turn scattered community knowledge into something easier to use, share, and reference.

The site is currently focused on **Havoc Hotel 3** and organizes stable community knowledge into clear sections such as:

- Overview
- Tips
- Tasks
- FAQ
- References
- Rescues
- Terms

[Access the help guide](https://docadam.github.io/TeraCreators-Help/)

## Community

Much of this guide is based on useful player and admin messages shared in the TeraCreators Discord community. If you want to join the community directly, use this invite:

[TeraCreators Discord](https://discord.gg/2Wra2xeC4J)

## What This Project Is

This site gathers community-shared help and turns it into documentation that is easier to browse than long chat threads.

The goal is to preserve useful gameplay information by compiling, curating, cataloging, condensing, contextualizing, and communicating it in a cleaner format for other players.

This includes:

- repeated gameplay advice
- step-by-step task instructions
- common player questions
- reference material
- game terms and shorthand
- rescue and progression notes

## What This Project Is Not

This guide does **not** try to preserve every message or every short-lived issue.

It intentionally prioritizes:

- stable gameplay help
- repeated or validated community knowledge
- practical information players can actually use

It generally excludes:

- temporary bugs
- one-off complaints
- fast-changing confusion
- unverified edge-case claims

## Local Development

Install dependencies from the project root:

```bash
npm install

Start the local development server from the project root:

npm run start

This usually starts the site at one of these URLs:
	•	http://localhost:3000/TeraCreators-Help/
	•	http://localhost:3000/

Build

Create a production build from the project root:

npm run build

This generates the static site in the build directory.

Deployment

This site is deployed with GitHub Pages using GitHub Actions.

When changes are pushed to the main branch, GitHub Actions builds and deploys the site automatically.

Live Site

https://docadam.github.io/TeraCreators-Help/

Project Structure

docs/
  intro.md
  havoc-hotel-3/
    overview.md
    tips.md
    tasks.md
    faq.md
    references.md
    rescues.md
    terms.md

.github/
  workflows/
    deploy.yml

Notes
	•	This guide is based on community-shared information
	•	Content is compiled from messages and reorganized into more usable documentation
	•	Stable gameplay help is prioritized over temporary bugs or one-off issues
	•	Some strategies are player-tested and may change as the game evolves
	•	Reported codes and rewards should be treated as community-maintained information

Tech Stack
	•	Docusaurus
	•	GitHub Pages
	•	GitHub Actions

Then run this from your project root:

```bash
npm run build

If the build succeeds, commit and push:

git add README.md
git commit -m "Update README with community-sourced project description"
git push