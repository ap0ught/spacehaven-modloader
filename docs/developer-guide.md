---
layout: default
title: Developer Guide
nav_order: 5
---

# Developer Guide
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Purpose

This guide explains how to set up a development environment to run the mod loader from source and contribute to the project.

---

## Prerequisites

- **uv** — fast Python package manager: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)
- **Python 3.11.9** — managed automatically by uv (or via [pyenv](https://github.com/pyenv/pyenv))
- **Git** — to clone the repository

---

## Cloning the Repository

```shell
git clone https://github.com/ap0ught/spacehaven-modloader.git
cd spacehaven-modloader
```

For the remainder of this guide, the working directory is the root of the repository.

---

## Installing Python

The repository includes a `.python-version` file pinning Python to a specific version. If you don't have it installed, use pyenv:

```shell
pyenv install 3.11.9
```

---

## Setting Up a Virtual Environment

Create and activate a Python virtual environment using uv:

```shell
uv venv
source .venv/bin/activate       # macOS / Linux
# or
.venv\Scripts\activate          # Windows (Command Prompt)
# or
.venv\Scripts\Activate.ps1      # Windows (PowerShell)
```

Install runtime dependencies:

```shell
uv pip install -r requirements.txt
```

---

## Running the Loader

With the virtual environment active:

```shell
python spacehaven-modloader.py
```

You can also run without activating the environment:

```shell
.venv/bin/python spacehaven-modloader.py     # macOS / Linux
.venv\Scripts\python spacehaven-modloader.py # Windows
```

---

## Running Tests

```shell
python -m unittest discover tests
```

---

## Code Style

The project uses [Black](https://black.readthedocs.io/) for formatting and [Flake8](https://flake8.pycqa.org/) for linting. Install them with:

```shell
uv pip install black flake8
```

Run the formatter:

```shell
black .
```

Run the linter:

```shell
flake8 .
```

Configuration is in `setup.cfg` and `.flake8`.

---

## Building a Release

### Windows

```powershell
# Install dependencies
uv pip install -r requirements.txt

# Build cx_Freeze executable
python setup.py build

# Generate NSIS file list
python generate_nsis_filelist.py

# Build NSIS installer (requires NSIS installed)
& "C:\Program Files (x86)\NSIS\makensis.exe" installer.nsi
```

The installer will be written to `dist/`.

### macOS

```shell
bash tools/build-macos.sh
```

---

## Project Structure

```
spacehaven-modloader/
├── spacehaven-modloader.py    Main entry point / UI
├── version.py                 Version string
├── setup.py                   cx_Freeze build configuration
├── generate_nsis_filelist.py  Generates NSIS installer file list
├── installer_template.nsi     NSIS installer template
├── modloader.spec             PyInstaller spec file
├── requirements.txt           Pinned runtime dependencies
├── requirements.in            Top-level dependency declarations
├── textures_annotations.xml   Texture annotation data
├── aspectj-1.9.19.jar         AspectJ compiler
├── aspectjweaver-1.9.19.jar   AspectJ weaver agent
├── loader/
│   ├── extract.py             Game asset extraction
│   ├── load.py                Mod loading / unloading
│   └── assets/
│       ├── annotate.py        XML annotation
│       ├── explode.py         Texture unpacking
│       ├── library.py         JAR manipulation
│       ├── merge.py           Mod merging logic
│       └── patch.py           Patch operations engine
├── ui/
│   ├── database.py            Mod database
│   ├── gameinfo.py            Game path detection
│   ├── header.py              UI header component
│   ├── launcher.py            Game launch logic
│   ├── log.py                 Log output
│   └── scrolledlistbox.py     Custom list widget
├── mods/                      Sample mods
├── tests/                     Unit tests
├── tools/                     Build scripts and assets
└── docs/                      GitHub Pages site (this site)
```

---

## CI / CD

The repository uses GitHub Actions for continuous integration and deployment:

| Workflow | Trigger | Description |
|----------|---------|-------------|
| `build.yml` | Push to `master`, Release published | Builds the Windows installer and uploads to the release |
| `pages.yml` | Push to `master`, Pull request | Builds this documentation site; deploys to GitHub Pages on push to `master` |

---

## Contributing

1. Fork the repository and create a feature branch.
2. Make your changes, following the code style guidelines above.
3. Add or update tests as appropriate.
4. Run tests and linting locally before opening a pull request.
5. Open a pull request against `master`.
