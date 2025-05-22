# Contributing Guide

Thank you for considering contributing to this project! This document outlines the workflow and best practices for proposing changes.

## Branching Strategy

* The `main` branch contains stable code. All development work should occur in feature branches created from `main`.
* Name your branch descriptively, for example `feat/chat-endpoint` or `fix/login-bug`.
* When your work is complete, open a pull request (PR) targeting `main`.
* Keep your branch focused on a single concern whenever possible.

## Commit Messages

We use a simplified convention inspired by the Angular commit style:

```
type(scope?): summary

[Optional body]
```

Common types include `feat`, `fix`, `docs`, and `chore`. The summary should be written in the imperative mood and kept under 72 characters.

Example:

```
feat(auth): add SSO callback handler
```

## Proposing Changes

1. Create a GitHub issue or comment on an existing one to discuss the change you would like to make.
2. Fork the repository or create a new branch if you have write access.
3. Commit your work following the message format described above.
4. Push your branch and open a PR against `main`.
5. Ensure your PR description explains the reason for the change and references any related issues.

By following these guidelines, you help us maintain a clean history and review process. We appreciate your contributions!
