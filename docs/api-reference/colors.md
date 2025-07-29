# Colors API

This section contains the API reference for **Colors** sub-module.

---

## **get_material_color**

Returns a dictionary of all shades of a material color

```python
get_material_color(color: str)
```

**Parameters:**

-   **`color`**: A color name from [**Material Colors**](../useful-to-know.md#material-colors)

**Returns:**

-   **`dict | None`**: A dictionary of corresponding color shades if found, otherwise `None`

---

## **get_web_colors**

Yields color dicts from web color list.

```python
get_web_colors()
```

**Returns:**

-   **`Generator[Dict]`**: A generator that yields [**HTML Colors**](https://materialui.co/htmlcolors) in a `dictionary` on each iteration.



## **get_palettes**

Yields predefined color palettes.

```python
get_palettes()
```

**Returns:**

-   **`Generator[List[str]]`**: A generator that yields a predefined color palette as a `list` on each iteration.


## **get_random_palette**

Get a random palette from all predefined colors palettes.

```python
get_random_palette()
```

**Returns:**

-   **`List[str]`**: A predefined color palette. _(list of hex colors)_
