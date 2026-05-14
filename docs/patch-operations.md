---
layout: default
title: Patch Operations
nav_order: 4
---

# Patch Operations
{: .no_toc }

Patch operations let you modify specific parts of the game library using XPath selectors without replacing entire definitions. They are applied **after** XML mod merging, which means they can modify both base game definitions and definitions added by other mods.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## File Structure

Patch files are stored in your mod's `patches/` folder. Each file must contain a root XML element wrapping one or more `<Operation>` elements:

```xml
<Patches>
    <Operation Class="AttributeSet">
        <xpath>//me[@mid="927"]</xpath>
        <attribute>someAttr</attribute>
        <value>newValue</value>
    </Operation>

    <Operation Class="NodeAdd">
        <xpath>//me[@mid="927"]</xpath>
        <value>
            <newChild attr="val" />
        </value>
    </Operation>
</Patches>
```

---

## Common Fields

Every patch operation shares these fields:

| Field | Description |
|-------|-------------|
| `Class` | (attribute) The operation type (see below) |
| `<xpath>` | XPath expression selecting the target node(s) |
| `<value>` | The value or node to apply (type depends on operation) |
| `<attribute>` | The attribute name to target (attribute operations only) |
| `<enable>` | Optional. If the value evaluates to false (`0`, `false`, `no`, `off`, `f`, `n`), the patch is skipped |
| `<disable>` | Optional. If the value evaluates to true (`1`, `true`, `yes`, `on`, `t`, `y`), the patch is skipped |

{: .note }
Both `<enable>` and `<disable>` support [mod config variables](modding-guide.md#mod-config-variables). This lets users toggle patches on/off via the mod loader UI.

---

## Attribute Operations

### `AttributeSet` / `SetAttribute`

Sets an attribute on the matching node(s). Adds the attribute if it doesn't exist, or overwrites it if it does.

```xml
<Operation Class="AttributeSet">
  <xpath>//crop[@id="1234"]</xpath>
  <attribute>growSpeed</attribute>
  <value>2.0</value>
</Operation>
```

---

### `AttributeAdd` / `AddAttribute`

Adds an attribute to the matching node(s), **only if the attribute does not already exist**. Raises an error if the attribute is already present.

```xml
<Operation Class="AttributeAdd">
  <xpath>//building[@id="500"]</xpath>
  <attribute>newFlag</attribute>
  <value>true</value>
</Operation>
```

---

### `AttributeRemove` / `RemoveAttribute`

Removes an attribute from the matching node(s).

```xml
<Operation Class="AttributeRemove">
  <xpath>//item[@id="300"]</xpath>
  <attribute>obsoleteAttr</attribute>
</Operation>
```

---

### `AttributeMath` / `MathAttribute`

Modifies a numeric attribute using arithmetic. Requires an `opType` attribute on `<value>`.

| `opType` | Operation |
|----------|-----------|
| `add` | `currentValue + value` |
| `subtract` | `currentValue - value` |
| `multiply` | `currentValue * value` |
| `divide` | `currentValue / value` |

```xml
<Operation Class="AttributeMath">
  <xpath>//crop[@id="1234"]</xpath>
  <attribute>growSpeed</attribute>
  <value opType="multiply">1.5</value>
</Operation>
```

{: .note }
If the original attribute contains a decimal point, the result is written with one decimal place. Otherwise the result is written as an integer.

---

## Node Operations

### `NodeAdd` / `AddNode` / `Add` / `NodeAddLast`

Adds the provided node(s) as the **last child** of the matching node(s).

```xml
<Operation Class="NodeAdd">
  <xpath>//building[@id="500"]/requirements</xpath>
  <value>
    <req resourceId="42" amount="5" />
  </value>
</Operation>
```

---

### `NodeAddFirst` / `AddFirst` / `AddNodeFirst`

Adds the provided node(s) as the **first child** of the matching node(s).

```xml
<Operation Class="NodeAddFirst">
  <xpath>//building[@id="500"]/requirements</xpath>
  <value>
    <req resourceId="1" amount="1" />
  </value>
</Operation>
```

---

### `NodeInsert` / `Insert` / `InsertNode` / `InsertAfter` / `NodeInsertAfter`

Inserts the provided node(s) as siblings **after** the matching node(s).

```xml
<Operation Class="NodeInsert">
  <xpath>//me[@mid="927"]</xpath>
  <value>
    <me mid="928" name="NewBuilding" />
  </value>
</Operation>
```

---

### `NodeInsertBefore` / `InsertBefore` / `InsertNodeBefore`

Inserts the provided node(s) as siblings **before** the matching node(s).

```xml
<Operation Class="NodeInsertBefore">
  <xpath>//me[@mid="927"]</xpath>
  <value>
    <me mid="926" name="EarlierBuilding" />
  </value>
</Operation>
```

---

### `NodeRemove` / `Remove` / `RemoveNode`

Removes the matching node(s) from the tree.

```xml
<Operation Class="NodeRemove">
  <xpath>//me[@mid="999"]</xpath>
</Operation>
```

---

### `NodeReplace` / `Replace` / `ReplaceNode`

Replaces the matching node(s) with a single provided node.

```xml
<Operation Class="NodeReplace">
  <xpath>//me[@mid="200"]</xpath>
  <value>
    <me mid="200" name="Replacement" someAttr="val" />
  </value>
</Operation>
```

{: .important }
`NodeReplace` requires exactly one child node inside `<value>`.

---

## Disabling a Patch File

Add a `<Noload />` element anywhere in the root of a patch file to prevent the entire file from loading. This is useful for patches under development or optional content:

```xml
<Patches>
  <Noload />
  <!-- These operations will not run -->
  <Operation Class="AttributeSet">
    ...
  </Operation>
</Patches>
```

---

## Tips

- Use `library/haven_annotated.xml` (generated by the **Annotate XML** button in the mod loader) to find the XPath for the element you want to modify.
- Patches are applied in mod load order, so patches in later mods can modify definitions from earlier mods.
- If an XPath expression matches zero elements, the patch is silently skipped (no error).
- Patch errors are logged to `mods/logs.txt`.
