# TeraCreators Help

A community-sourced help guide for TeraCreators games, built from compiled Discord messages and then curated into clearer, more practical documentation for players.

This project was made by someone who genuinely enjoys playing these games and wanted to turn scattered community knowledge into something easier to use, search, share, and reference.

[Access the help guide](https://docadam.github.io/TeraCreators-Help/)

## Current Game Sections

The site is currently organized around these game sections:

- Havoc Hotel 3
- Havoc Hotel 2
- Havoc Hotel 1
- Raptor Heist

Each game section is broken into practical documentation pages such as:

- Overview
- Tips
- Tasks
- FAQ
- References
- Terms

Some games may also include additional sections where needed, such as:

- Rescues

## Community

Much of this guide is based on useful player and admin messages shared in the TeraCreators Discord community.

If you want to join the community directly, use this invite:

[TeraCreators Discord](https://discord.gg/2Wra2xeC4J)

## What This Project Is

This site gathers community-shared help and turns it into documentation that is easier to browse than long chat threads.

The goal is to preserve useful gameplay information by compiling, curating, consolidating, clarifying, and organizing it into a cleaner format for other players.

This includes:

- repeated gameplay advice
- step-by-step task instructions
- common player questions
- reference material
- game terms and shorthand
- rescue and progression notes where applicable

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

## Site Structure

The current sidebar layout is:

- Havoc Hotel 3
  - Overview
  - Tips
  - Tasks
  - FAQ
  - References
  - Rescues
  - Terms
- Havoc Hotel 2
  - Overview
  - Tips
  - Tasks
  - FAQ
  - References
  - Terms
- Havoc Hotel 1
  - Overview
  - Tips
  - Tasks
  - FAQ
  - References
  - Terms
- Raptor Heist
  - Overview
  - Tips
  - Tasks
  - FAQ
  - References
  - Terms

## Project Structure

```text
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
  havoc-hotel-2/
    overview.md
    tips.md
    tasks.md
    faq.md
    references.md
    terms.md
  havoc-hotel-1/
    overview.md
    tips.md
    tasks.md
    faq.md
    references.md
    terms.md
  raptor/
    overview.md
    tips.md
    tasks.md
    faq.md
    references.md
    terms.md

static/
  img/
    havoc-hotel-3/
    havoc-hotel-2/
    havoc-hotel-1/
    raptor/

.github/
  workflows/
    deploy.yml

## Local Development

Install dependencies from the project root:

```bash
npm install
```

Start the local development server from the project root:

```
npm run start
```

This usually starts the site at one of these URLs:
- http://localhost:3000/TeraCreators-Help/
- http://localhost:3000/

## Build

Create a production build from the project root:

```
npm run build
```

This generates the static site in the build directory.

## Deployment

This site is deployed with GitHub Pages using GitHub Actions.

When changes are pushed to the main branch, GitHub Actions builds and deploys the site automatically.

## Live Site

https://docadam.github.io/TeraCreators-Help/￼

### Notes

- This guide is based on community-shared information
- Content is compiled from messages and reorganized into more usable documentation
- Stable gameplay help is prioritized over temporary bugs or one-off issues
- Some strategies are player-tested and may change as the game evolves
- Reported codes and rewards should be treated as community-maintained information

### Tech Stack
- Docusaurus
- GitHub Pages
- GitHub Actions