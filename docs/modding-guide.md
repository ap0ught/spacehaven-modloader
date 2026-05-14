---
layout: default
title: Modding Guide
nav_order: 3
---

# Modding Guide
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Mod Types

The mod loader supports three types of mods:

| Type | Description |
|------|-------------|
| **XML Mods** | Merge new or replacement definitions into the game library |
| **Patch Operations** | Surgically modify existing definitions using XPath |
| **Code Injection Mods** | Inject Java code using AspectJ |

---

## Mod Structure

Every mod lives in its own folder inside the `mods/` directory. At minimum, a mod must contain an `info.xml` file.

```
mods/
  YourModName/
    info.xml            ← required: mod metadata
    library/            ← XML library files (XML mods)
      haven.xml
      animations.xml
      textures.xml
      texts.xml
      audio.xml
    patches/            ← patch operation files
      my_patch.xml
    textures/           ← texture images
      12345.png
    YourMod.jar         ← compiled code injection mod (optional)
```

---

## info.xml

The `info.xml` file describes your mod:

```xml
<mod>
  <name>Your Mod Name</name>
  <modid>yourmodid</modid>
  <description>A short description of your mod.</description>
  <minimumLoaderVersion>0.0.1</minimumLoaderVersion>
  <gameVersions>
    <v>0.4.1</v>
  </gameVersions>
  <config>
    <variable name="MY_VARIABLE" default="1.5" description="A configurable value" />
  </config>
</mod>
```

| Tag | Required | Description |
|-----|----------|-------------|
| `<name>` | Yes | Display name shown in the mod loader |
| `<modid>` | Recommended | Unique identifier used for texture packing and variable prefixes |
| `<description>` | No | Description shown in the mod loader |
| `<minimumLoaderVersion>` | No | Minimum mod loader version required |
| `<gameVersions>` | No | Compatible game versions |
| `<config>` | No | User-configurable variables (see [Mod Config Variables](#mod-config-variables)) |

---

## XML Mods

XML mods merge new or replacement definitions into the game library. They follow the same format as the game's built-in library.

### Supported Files and Tags

| File | Supported elements |
|------|--------------------|
| `library/haven` | All definitions |
| `library/animations` | `<animations>` entries |
| `library/textures` | `<t>` and `<re>` entries |
| `library/texts` | `<t>` entries |
| `library/audio` | Audio definitions |

### ID Numbers

Most game definitions use numeric IDs rather than human-readable names. The mod loader merges your definitions **by ID**, so:

- **Replacing** an existing definition: use the same ID as the game uses.
- **Adding** a new definition: choose a unique ID.

{: .important }
IDs are 32-bit integers shared across all loaded mods. To avoid conflicts, prefix your IDs with your Discord user number followed by a sequential mod number. For example, if your Discord ID is `#4511` and this is your first mod (`00`), use IDs like `451100000`, `451100001`, `451100002`, etc.

### Navigating the Library

After extracting and annotating game assets, open `mods/spacehaven/library/haven_annotated.xml`. This file adds `_annotated_name=""` attributes to make navigation easier.

**Finding a definition by name:**

1. Search for the name in `library/texts`.
2. Find the `id="..."` attribute on that text entry.
3. Search for `tid="<that id>"` in `library/haven_annotated.xml`.

**Example:** Finding the "Life Support" building

```xml
<!-- In library/texts: -->
<lifeSupportName id="140" pid="139">
    <EN>Life Support</EN>
</lifeSupportName>

<!-- Search for tid="140" in library/haven_annotated.xml: -->
<me mid="927" ...>
    <objectInfo ...>
        <name tid="140" />
        <desc tid="141" />
        <subCat id="1508" />
    </objectInfo>
</me>
```

Here `mid="927"` is the Life Support unit's ID.

---

## Textures and Animations

### Extracting Textures

Clicking **Annotate XML** also unpacks all textures into `mods/spacehaven/library/textures.exploded/`:

- `textures.exploded/*.png` — original packed texture atlases
- `textures.exploded/<textureID>/<regionID>.png` — individual texture regions

### Replacing a Texture

Place a file named `<textureID>.png` in your mod's `textures/` folder. For example, to replace texture `123`:

```
mods/YourMod/textures/123.png
```

### Adding a New Texture

1. Add a `<re n="..." t="..." />` entry in your `library/textures.xml`, referencing a `<t i="..." />` entry.
2. Place the image file in `textures/` named after the region ID.

The loader packs your images and outputs a debug PNG when loading your mod so you can verify placement.

### Auto-Packing Textures

If your mod has a `<modid>` set in `info.xml`, you can skip defining a `textures` file. Instead, add a `filename=""` attribute to `<assetPos />` tags in `library/animations.xml`. The loader will pack these automatically into `<modid>.cim`.

---

## Patch Operations

Patch operations let you surgically modify specific parts of the game library without replacing entire definitions. They are stored in the `patches/` folder.

See the full [Patch Operations reference](patch-operations.md) for details.

---

## Mod Config Variables

Variables allow users to configure your mod from the mod loader UI without editing files.

### Defining Variables

Add a `<config>` section to your `info.xml`:

```xml
<config>
  <variable name="CROP_SPEED" default="1.5" description="Growth speed multiplier" />
  <variable name="MAX_TEMP" default="40" description="Maximum temperature (°C)" />
</config>
```

### Using Variables in Patches

Reference variable names in your patch `<value>` text. The loader substitutes values before applying:

```xml
<Operation Class="AttributeSet">
  <xpath>//crop[@id="1234"]</xpath>
  <attribute>speed</attribute>
  <value>CROP_SPEED</value>
</Operation>
```

{: .warning }
Variables are simple text substitutions. There is currently no UI validation of variable values.

---

## Code Injection Mods

Code injection mods use [AspectJ](https://www.eclipse.org/aspectj/) (similar to Harmony in C#) to intercept and modify game methods.

These mods are compiled to a `.jar` file and placed in the mod folder alongside `info.xml`.

### Getting Started

Use the [SpaceHavenModTemplate](https://github.com/Spacehaven-modding-tools/SpaceHavenModTemplate) as a starting point. It includes:

- Dev environment setup instructions
- Sample mods demonstrating common patterns

### Decompiling the Game

You'll need to inspect the game's source code. [JD-GUI](https://github.com/java-decompiler/jd-gui) works well. The game is not obfuscated.

---

## Sample Mods

The repository includes several example mods in the `mods/` directory:

| Mod | Type | Description |
|-----|------|-------------|
| `greenhouse` | XML | Rebalances crop growth using temperature and gas systems |
| `exterior-air-vent` | XML | Adds an exterior air vent building |
| `Electric Slide` | Config | Demonstrates mod config variables |
