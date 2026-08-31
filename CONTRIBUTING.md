# Contributing

Thanks for contributing to this Python/Pygame project. Please keep changes focused and explain the user-facing or gameplay impact in your pull request.

## Setup

You need Python 3.9 or newer and Pygame.

```bash
python --version
python -m pip install pygame
```

Clone the repository before making changes:

```bash
git clone <repository-url>
cd <repository-directory>
```

The repository contains two runnable game examples. Start the one you want to work on with either `python space_shooter.py` or `python doodleblock.py`.

## Branching

Create a focused branch from the current default branch. Use a short, descriptive name, such as `fix-player-movement` or `docs-contributing`.

Keep unrelated changes out of the branch, and rebase or update it from the default branch before opening a pull request when necessary.

## Testing

No automated test suite is currently documented. Run the game script you changed and manually check the relevant controls, gameplay behavior, and exit behavior.

For documentation-only changes, run:

```bash
git diff --check
```

Do not commit generated files, secrets, or unrelated formatting changes.

## Pull Requests

Open a pull request against the default branch after checking your changes locally. Describe what changed, how you tested it, and any limitations or follow-up work. Keep each pull request focused on one issue, and include screenshots or a short recording when they help explain a gameplay or visual change.

## Code of Conduct

Be respectful, constructive, and inclusive. Do not harass, discriminate against, or demean other contributors. Keep project discussions focused on improving the software, and raise concerns with the project maintainers.
