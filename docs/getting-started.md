---
layout: default
title: Getting Started
nav_order: 2
---

# Getting Started
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Installation

1. Go to the [Releases page](https://github.com/ap0ught/spacehaven-modloader/releases) and download the latest installer for your platform.
2. Run the installer and follow the prompts.
3. Launch **Space Haven Mod Loader** from the Start Menu (Windows) or Applications folder (macOS).

---

## First-time setup

![Screenshot](https://github.com/ap0ught/spacehaven-modloader/raw/master/tools/screenshot.png)

### Locating Space Haven

The mod loader will try to find your Space Haven installation automatically. If it can't, click **Browse…** in the top-right corner and navigate to:

| Platform | Typical location |
|----------|-----------------|
| Windows (Steam) | `C:\Program Files (x86)\Steam\steamapps\common\SpaceHaven\spacehaven.exe` |
| macOS | `/Applications/spacehaven.app` or `/Applications/Games/spacehaven.app` |
| Linux (Steam) | `~/.local/share/Steam/steamapps/common/SpaceHaven/spacehaven` |

---

## Installing Mods

1. Click **Open Mods Folder** to open your game's `mods` folder in the file explorer.
2. Download mods from [NexusMods](https://www.nexusmods.com/spacehaven) and copy them into the `mods` folder.

Your game folder should look something like this when mods are installed:

```
spacehaven.jar
savegames/
  ...
mods/
  BetterToilets/
    info.xml
    library/
      haven.xml
      animations.xml
      textures.xml
    textures/
      2283.png
  ClaimDerelict/
    info.xml
    ClaimDerelict.jar
  ...
```

3. Return to the mod loader. Your mods should appear in the list. If they don't, double-check the folder structure above.

4. Make sure the mods you want active are checked/enabled in the list.

5. Click **Launch Space Haven!** to play. The mod loader will:
   - Merge mods into the game JAR
   - Launch the game
   - Restore the original JAR when you exit

---

## QuickLaunch

After playing with a given set of mods, the loader saves a **QuickLaunch file** so subsequent launches are much faster.

{: .important }
If you are developing a mod or have made changes to a mod, click **Clear QuickLaunch file** before launching the game so your changes are picked up.

---

## Extracting & Annotating Game Assets

The mod loader can unpack the game's library for browsing and modding:

- **Extract game assets** — extracts `spacehaven.jar` into `mods/spacehaven/` and opens the folder.
- **Annotate XML** — creates human-readable annotated versions of the library files:
  - `library/haven_annotated.xml` — main game library with `_annotated_name` attributes
  - `library/animations_annotated.xml` — animations with texture name hints

These annotated files are the starting point for creating XML mods. See the [Modding Guide](modding-guide.md) for details.

---

## Known Issues

- If you change the language or restart the game from within itself, the mod loader will think the game has quit and may throw an error. Nothing is permanently broken.
- Running the game from the mod loader does not load cloud credentials correctly.
