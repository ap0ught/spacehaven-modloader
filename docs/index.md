---
layout: home
title: Home
nav_order: 1
---

# Space Haven Mod Loader

A modding tool for [Space Haven by Bugbyte](http://bugbyte.fi/spacehaven/), a spaceship colony sim.

[![Latest Release](https://img.shields.io/github/v/release/ap0ught/spacehaven-modloader)](https://github.com/ap0ught/spacehaven-modloader/releases)
[![License](https://img.shields.io/github/license/ap0ught/spacehaven-modloader)](https://github.com/ap0ught/spacehaven-modloader/blob/master/LICENSE)

---

## What is it?

The Space Haven Mod Loader makes it easy to install and manage mods for Space Haven. It handles loading mods into the game's JAR file before launch and cleanly restoring the original files when the game exits.

**Supported mod types:**

- **XML Mods** — modify game data such as buildings, items, ships, characters, and more by merging XML definitions with the game library.
- **Patch Operations** — surgically alter existing game definitions using XPath-targeted patch instructions.
- **Code Injection Mods** — use AspectJ to inject custom Java code before, after, or around existing game methods.
- **Texture Mods** — replace or add new packed textures (`.cim` files).

---

## Quick Links

| Page | Description |
|------|-------------|
| [Getting Started]({% link getting-started.md %}) | Download, install, and run your first mod |
| [Modding Guide]({% link modding-guide.md %}) | Create XML mods and understand the game library |
| [Patch Operations]({% link patch-operations.md %}) | Reference for all supported patch operations |
| [Developer Guide]({% link developer-guide.md %}) | Set up a development environment and contribute |
| [Changelog]({% link changelog.md %}) | Version history and release notes |

---

## Screenshot

![Space Haven Mod Loader Screenshot](https://github.com/ap0ught/spacehaven-modloader/raw/master/tools/screenshot.png)

---

## Community

- Mods can be found on [NexusMods](https://www.nexusmods.com/spacehaven)
- Code injection mod template: [SpaceHavenModTemplate](https://github.com/ap0ught/SpaceHavenModTemplate)
- Report bugs and request features on [GitHub Issues](https://github.com/ap0ught/spacehaven-modloader/issues)
