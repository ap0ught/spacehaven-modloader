---
layout: default
title: Changelog
nav_order: 6
---

# Changelog

---

## v0.12.4

- Version bump

---

## v0.12.1

- Fix build missing annotate code

---

## v0.12.0

### New Modifiable Stuff
- Added modding of `library/audio`

### Engine
- Improved patch operations log and validations
- Added new patch operations

### Source Code Improvements
- Deleted some deprecated mod examples (mods on Nexus serve as a better demo)
- Cleanup of unused Python modules in source code → smaller `requirements.txt`
- Upgraded Python to version 3.11.9
- Fixed zipfile error ("zip bomb") when upgrading Python
- Fixed all lxml warnings
- Fixed build/dist scripts
- Fixed launch VSCode options
- Added `black` and `flake8` for clean development
- Fixes and coding style changes due to `black` and `flake8`
- Removed unused variable declarations from `spacehaven-modloader.py`
- Improved `.gitignore`

---

## v0.10.0

### GitHub Issues Resolved
- [#4](https://github.com/ap0ught/spacehaven-modloader/issues/4) Add mod configuration options
- [#5](https://github.com/ap0ught/spacehaven-modloader/issues/5) Possible issue during CIM generation
- [#7](https://github.com/ap0ught/spacehaven-modloader/issues/7) Patch operation Add doesn't adhere to the PatchOperationAdd standard
- [#19](https://github.com/ap0ught/spacehaven-modloader/issues/19) Mod loader issue

### UI Changes
- List box now has a scrollbar
- Description frame now has a scrollbar
- List box and description can be resized
- Small window sizes are handled better
- Default window size increased

### New Modifiable Sections
- Explosion
- FloorExpPackage
- GameScenario
- Robot
- RoofExpPackage
- Tech
- TechTree

### Mod Config Variables
- Modders can create variables that are user-configurable
- Variable values are saved at launch time
- Variables can be reset to defaults
- Example mods included: "Electric Slide", "Engine Tuner", and "Robot Work"
- **Known issue:** Variables do not have UI validation
- **Known issue:** All variables are a simple search-replace

### Improved Annotations
- `Element` entries now have a `_linkedBy` attribute listing what elements link to them
- `Element` entries that produce or consume a resource now annotate that resource with its name
- `Product` entries now have annotations for their needs and output
- `DataLogFragment` now have an annotation with the file path
- `GameScenario` now have name annotation
- `SubCat` now have annotations
- `PersonalitySettings/attributes/l` now annotated
- `DifficultySettings` now have annotation for all resources and items
- `Faction` entries now annotated
- `Craft` now have name annotation
- `DataLog` now have name annotation
- `BackStory` now have name annotation
- `TradingValues` entries now annotated with resource name
- `CharacterTrait` now have name annotation
- `CharacterCondition` now have name annotation
- `MainCat` now have annotations
- `TechTree` entries now have items annotation
- `Robot` cost and repair elements are annotated with element name

### Other
- Removed dependency on the `steamfiles` pip module

---

## v0.9.1

- **Bugfix:** `AttributeAdd` patch operations were universally failing due to a missing variable

---

## v0.9.0

- On Windows, the game is auto-located via Steam if possible
- `<modid>` tag in `info.xml`: Defines a prefix for use during mod creation
- **Automatic texture packing:** Texture regions can be defined as needed in `animations` — add a `filename=""` attribute to the `<assetPos />` tag and it will be packed automatically into `<modid>.cim` (requires a `<modid>`)
- Automatic texture patching writes the resulting textures XML to `moddir/library/generated_textures.xml` for debugging
- Attempt to normalize file paths across the codebase
- More log cleanup — less noise, better error messages
- Decouple mod database from window class
- Decouple mod info from window class

---

## v0.8.2

- **Bugfix:** Textures were not being merged in due to a missing file during the build process

---

## v0.8.1

- **New patch operation:** `AttributeMath` (not in the PatchOperation specification)
  - Requires an `opType` attribute on the `<value />` tag
  - Supported operations: `add`, `subtract`, `multiply`, `divide`
- `<Noload />` tag — prevents a patch file from loading (useful for optional patches or patches in development)
- General code refactoring

---

## v0.0.8

Support for [PatchOperation](https://rimworldwiki.com/wiki/Modding_Tutorials/PatchOperations) modding:

- `AttributeSet` → `PatchOperationAttributeSet`
- `AttributeAdd` → `PatchOperationAttributeAdd`
- `AttributeRemove` → `PatchOperationAttributeRemove`
- `Add` → `PatchOperationAdd`
- `Insert` → `PatchOperationInsert`
- `Remove` → `PatchOperationRemove`
- `Replace` → `PatchOperationReplace`

Patches are loaded from `moddir/patches/`, applied after merge-by-id to allow modding other mods without clobbering.
Patch failures are logged to `logs.txt`.

---

## v0.0.2

- Adds support for patching all definitions in `library/haven`, not just `Elements` and `Products`
- Fixed a typo in the launch button ("Spacehaven" → "Space Haven")
- Adds logging to `mods/logs.txt`
- Adds game version checking and warnings

---

## v0.0.1

Initial release.
