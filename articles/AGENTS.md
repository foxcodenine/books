# AGENTS.md

## Purpose

This directory is a personal study collection for technical articles. Each article may contain:

- a link to the original source;
- personal notes and summaries;
- an optional PDF saved by the repository owner;
- runnable code written while working through the article.

Keep article work self-contained inside `articles/` unless the user explicitly asks for changes elsewhere in the repository.

## Directory structure

Organize articles by subject and then by a concise, kebab-case article slug:

```text
articles/
├── README.md
├── <language-or-topic>/
│   └── <subtopic>/
│       └── <article-slug>/
│           ├── README.md
│           ├── article.pdf      # optional; only when supplied or requested
│           └── code/
└── AGENTS.md
```

Use existing categories when possible. Create a new category only when none of the current categories describes the article well.

## Adding an article

When asked to add an article:

1. Open the source URL and verify its title, author, and subject when web access is available.
2. Choose a short, descriptive, kebab-case directory name.
3. Create an article `README.md` using the template below.
4. Create `code/` only when exercises or examples are expected. Add `.gitkeep` while it is empty.
5. Add the article to the appropriate section of `articles/README.md`.
6. Do not create an empty or fake PDF placeholder.
7. Show the resulting tree and summarize what was added.

## Article README template

```markdown
# Article title

- Source: <canonical URL>
- Author: <author, if known>
- Status: To study
- Accessed: YYYY-MM-DD

## Goal

Explain what should be learned or built from this article.

## Notes

Write personal notes and summaries here.

## Code

Related examples and exercises belong in `code/`.
```

Use one of these status values consistently:

- `To study`
- `In progress`
- `Completed`
- `Reference`

## Notes and source material

- Write summaries in original words and clearly distinguish personal conclusions from claims made by the source.
- Preserve the canonical source URL in every article README.
- Do not copy large portions of an article into the repository.
- Keep short quotations clearly attributed.
- Do not download, generate, replace, or commit a PDF unless the user explicitly requests it and has the right to store it.
- Never treat a saved PDF as permission to redistribute copyrighted material.

## Code conventions

- Put article-specific implementations under that article's `code/` directory.
- Prefer small, runnable examples over disconnected snippets.
- Follow the standard formatter and conventions for the language being used.
- Add the smallest useful dependency or module file inside the article's `code/` directory when needed.
- Do not share dependencies between unrelated articles.
- Add focused tests when an example contains meaningful behavior.
- Run relevant formatting, tests, and static checks before reporting completion.
- Document commands needed to run the example in the article README.

## Repository hygiene

- Preserve unrelated user changes in this repository.
- Do not rename or reorganize existing article directories unless requested.
- Avoid committing generated caches, virtual environments, dependency directories, build output, logs, credentials, or secrets.
- Use relative Markdown links for files within this repository.
- Update `articles/README.md` whenever an article is added, moved, renamed, or removed.
- Keep filenames and directory names lowercase and kebab-case, except conventional names such as `README.md`, `AGENTS.md`, `Dockerfile`, and language-specific files.

## Verification

Before finishing article work:

- confirm every source link and local index link is correct;
- confirm the directory follows the established hierarchy;
- confirm no credentials or generated artifacts were introduced;
- run applicable code checks;
- report checks that could not be run and why.
