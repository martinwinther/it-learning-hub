# Installing Python

## Overview

Before writing and running Python programs, you must have a Python interpreter
installed on your system. The interpreter reads and executes Python code. Most
Linux and macOS systems come with Python pre-installed, but it may not be the
latest version. Windows does not include Python by default.

This section outlines how to download, install, and verify Python.

## Downloading Python

### Official Source

- Always download Python from the official website:
  [https://www.python.org](https://www.python.org).
- This ensures you get a safe, up-to-date version.
- Avoid third-party installers to reduce the risk of outdated or modified
  distributions.

### Choosing the Version

- **Python 3.x** is the current standard — this course uses Python 3.
- Do not use Python 2 unless working with legacy systems.

## Installation by Operating System

### Windows

- Download the Windows installer (`.exe`) from the official site.
- Run the installer and **check the box "Add Python to PATH"** before proceeding
  — this makes Python available from the command line.
- Complete installation by following prompts.
- Optional: Install `pip` (Python's package manager) if not included by default.

### macOS

- Download the macOS installer (`.pkg`) from the official site.
- Double-click to run and follow the instructions.
- Alternatively, install via package managers such as **Homebrew**:

  ```bash
  brew install python
  ```

### Linux

- Many distributions include Python by default.
- Check version:

  ```bash
  python3 --version
  ```

- Update or install via your distribution's package manager:
  - Debian/Ubuntu:

    ```bash
    sudo apt update
    sudo apt install python3
    ```

  - Fedora:

    ```bash
    sudo dnf install python3
    ```

## Verifying the Installation

### Check Version

- Open a terminal or command prompt and run:

  ```bash
  python3 --version
  ```

- This should display the installed Python version.

### Launch Interactive Shell

- Run:

  ```bash
  python3
  ```

- You will see the Python prompt (`>>>`), where you can type and execute Python
  commands interactively.

### Exit the Shell

- Use:

  ```python
  exit()
  ```

  or press `Ctrl+D` (Linux/macOS) / `Ctrl+Z` then Enter (Windows).

## Summary

- Install Python from [python.org](https://www.python.org) to ensure safety and
  compatibility.
- Always use **Python 3** for new projects.
- Installation steps vary slightly between Windows, macOS, and Linux.
- Verify the installation by checking the version and running the interactive
  shell.
