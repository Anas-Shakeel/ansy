# Ansy API

This section contains the full API reference for **Ansy**.

---

## **colored**

Colorize text using `4-bit`, `8-bit`, or `24-bit` color modes. Supports **4-bit** _(standard)_, **8-bit** _(extended)_, and **24-bit** _(true color)_ modes. If no formatting is provided, returns the plain text.

```py
colored(
    text: str,
    fgcolor: Color = None,
    bgcolor: Color = None,
    attrs: Iterable[Attribute] = None,
    color_mode: ColorMode = 4,
    *,
    no_color: bool = None,
    force_color: bool = None,
)
```

**Parameters:**

-   **`text`:** The text you want to format
-   **`fgcolor`:** Foreground color of the text
-   **`bgcolor`:** Background color of the text
-   **`attrs`:** Iterable of attributes to apply like `['bold', 'italic']`
-   **`color_mode`:** The color mode (`4`, `8`, or `24`). Default is `4`
-   **`no_color`:** Disable formatting
-   **`force_color`:** Force formatting regardless of terminal support

**Returns:**

-   **`str`**: A formatted string with colors and styles _(or plaintext)_

**Raises:**

-   **`ColorModeError`**: If `color_mode` is invalid
-   **`InvalidColorError`** If `fgcolor` or `bgcolor` is an invalid
-   **`AttributeError`**: If `attrs` contains an invalid attribute

!!! note
    If `fgcolor`, `bgcolor`, and `attrs` are all set to `None`, the text itself is returned without any ansi codes added.

---

## **printc**

Prints text to the terminal using `colored()` formatting. Supports all standard `print()` parameters along with color customization options.

```py
printc(
    text: str,
    fgcolor: Color = None,
    bgcolor: Color = None,
    attrs: Iterable[Attribute] = None,
    color_mode: ColorMode = 4,
    *,
    sep=" ",
    end="\n",
    file=None,
    flush=False,
    no_color: bool = None,
    force_color: bool = None,
)
```

It's a Shortcut for `print(colored(...))`.

---

## **colored_ansy**

Applies styles to parts of a string using Ansy syntax `@style_name[text]`.

```py
colored_ansy(
    text: str,
    style: dict,
    *,
    no_color: bool = None,
    force_color: bool = None,
)
```

**Parameters:**

-   **`text`:** The input string containing Ansy-style tags like `@style_name[text]`.
-   **`style`:** A dictionary mapping style names to style definitions. Each style definition must be a `dict` containing:
    -   **`color_mode: int`:** The color mode to use
    -   **`fgcolor: Color`:** Foreground color of the text
    -   **`bgcolor: Color`:** Background color of the text
    -   **`attrs: Iterable[Attribute]`:** An iterable of attributes. (**bold**, _italic_ etc.)
-   **`no_color`:** Disable formatting
-   **`force_color`:** Force formatting regardless of terminal support

**Returns:**

-   **`str`**: A formatted string

**Raises:**

-   **`StyleError`:** If `style` used in ansy string `text` is not found in `style` dict
-   **`ColorModeError`:** If `color_mode` provided in style is invalid

---

## **colored_gradient**

Applies a smooth horizontal gradient to text using **24-bit RGB** colors.

```python
colored_gradient(
    text: str,
    start_color: Union[RGBTuple, str],
    end_color: Union[RGBTuple, str],
    quality: Quality = "medium",
    reverse: bool = False,
)
```

**Parameters:**

-   **`text`**: The string to which the horizontal gradient will be applied
-   **`start_color`**: The starting color of the gradient. _(in either **RGB** tuple form or **HEX** string.)_
-   **`end_color`**: The ending color of the gradient
-   **`quality`**: The gradient quality. Options are `low`, `medium`, and `high`. _(Higher values generate smoother gradients but longer output strings)_
-   **`reverse`**: If `True`, flips the gradient

**Returns:**

-   **`str`**: A formatted string

**Raises:**

-   **`InvalidColorError`** If `start_color` or `end_color` is an invalid 24-bit color
-   **`AssertionError`** If:
    -   `quality` is not set to `high` or `medium` or `low`
    -   any of `start_color` or `end_color` are `None`

---

## **colored_random**

Applies random colors to **characters**, **words**, or the **entire string** using the specified color system. Optional support for random attributes and custom palettes.

```python
colored_random(
    text: str,
    target: Literal["all", "words", "chars"] = "all",
    color_mode: ColorMode = 4,
    custom_palette: Iterable = None,
    attrs: Iterable[Attribute] = None,
    random_attrs: bool = False,
)
```

**Parameters:**

-   **`text`**: Text to format
-   **`target`**: Defines how random colors are applied:
    -   `all`: apply one random color to the entire text
    -   `words`: apply different random colors to each word
    -   `chars`: apply different random colors to each characte
-   **`color_mode`**: Color system to use: `4`, `8`, or `24-bit`
-   **`custom_palette`**: A list of user-defined colors to choose from
-   **`attrs`**: Iterable of attributes to apply to all text. _(all attributes will be applied uniformely)_
-   **`random_attrs`**: If `True`, randomizes provided attributes `attrs` too

**Returns:**

-   **`str`**: A formatted string

**Raises:**

-   **`ValueError`**: If `target` is not set to `'chars'`, `'words'`, `'all'`
-   **`ColorModeError`**: If `color_mode` is invalid
-   **`InvalidColorError`**: If `custom_palette` contains an invalid color
-   **`AttributeError`**: If `attrs` contains an invalid attribute

---

## **de_ansi**

Removes all ANSI codes (colors and styles) from a string.

```python
de_ansi(text: str)
```

**Parameters:**

-   **`text`**: The input string from which ANSI escape sequences should be removed

**Returns:**

-   **`str`**: A plain, ANSI-free string

**Raises:**

-   **`TypeError`**: If `text` is not a string

---

## **make_ansi**

Generates Raw ANSI escape sequence based on the provided colors and attributes. _(Used internally by some functions)_

```python
make_ansi(
    fgcolor: Color = None,
    bgcolor: Color = None,
    attrs: Iterable[Attribute] = None,
    color_mode: ColorMode = 4,
)
```

**Parameters:**

-   **`fgcolor`**: The foreground color to apply. Must be valid within the specified `color_mode`
-   **`bgcolor`**: The background color to apply. Must be valid within the specified `color_mode`
-   **`attrs`**: Iterable of attributes to apply. For example: `["bold", "italic"]`
-   **`color_mode`**: Color system to use. Must be one of `4`, `8`, or `24`. _(Defaults to 4)_

**Returns:**

-   **`str`**: The ANSI escape sequence string. _(without the reset code)_

**Raises:**

-   **`InvalidColorError`** — If `fgcolor` or `bgcolor` is not valid in the given `color_mode`
-   **`ColorModeError`** — If `color_mode` is not one of `4`, `8`, or `24`

---

## **make_gradient**

Generates a gradient of RGB values interpolated between `start_color` to `end_color` over a number of steps. _(Used internally by `colored_gradient` function)_

```python
make_gradient(
    start_color: RGBTuple,
    end_color: RGBTuple,
    steps: int = 10,
    reverse: bool = False,
)
```

**Parameters:**

-   **`start_color`**: The starting color as an RGB tuple. _e.g. `(255, 0, 0)`_
-   **`end_color`**: The ending color as an RGB tuple. _e.g. `(0, 255, 0)`_
-   **`steps`**: Number of colors to generate between `start_color` and `end_color`. _(Must be at least 2)_
-   **`reverse`**: If True, the gradient is flipped horizontally. _(end → start)_

**Returns:**

-   **`generator[tuple[int, int, int]]`**: A generator that yields RGB tuples representing the gradient

**Raises:**

-   **`InvalidColorError`**: If `start_color` or `end_color` is not a valid RGB tuple

---

## **create_style**

Generates and validates a style dictionary for use in `colored_ansy()`.

```python
create_style(
    color_mode: ColorMode = 4,
    fgcolor: Color = None,
    bgcolor: Color = None,
    attrs: Iterable[Attribute] = None,
)
```

**Parameters:**

-   **`color_mode`**: The color mode to use
-   **`fgcolor`**: The foreground color. Must match the selected `color_mode`
-   **`bgcolor`**: The background color. Must match the selected `color_mode`
-   **`attrs`**: Iterable of attributes to apply. For example: `["bold", "italic"]`

**Returns:**

-   **`dict`**: A dictionary representing the validated style, usable with `colored_ansy()`

**Raises:**

-   **`InvalidColorError`**: If `fgcolor` or `bgcolor` is invalid
-   **`ColorModeError`**: If `color_mode` is invalid
-   **`AttributeError`**: If any value in `attrs` is not a valid attribute

---

## **create_random_palette**

Return a list of `n` random colors for the given color mode.

```python
create_random_palette(
    color_mode: ColorMode,
    n: int,
)
```

**Parameters:**

-   **`color_mode`**: The color mode to use
-   **`n`**: Number of colors to generate in the palette

**Returns:**

-   **`list[str | tuple[int, int, int]]`**: A list of randomly selected colors compatible with the specified color mode

**Raises:**

-   **`TypeError`**: If `n` is not an integer
-   **`ColorModeError`**: If `color_mode` is invalid

---

## **contains_ansi**

Check if a string contains ANSI escape codes.

```python
contains_ansi(text: str)
```

**Parameters:**

-   **`text`**: The string to check for ANSI escape codes
-   **`n`**: Number of colors to generate in the palette

**Returns:**

-   **`bool`**: `True` if ANSI codes are present in the string, otherwise `False`

**Raises:**

-   **`TypeError`**: If `text` is not a string

---

## **get_random_color**

Returns a random color from the selected color mode. Output may be a color name or an RGB tuple depending on the mode.

```python
get_random_color(color_mode: ColorMode = 4)
```

**Parameters:**

-   **`color_mode`**: The color mode to use

**Returns:**

-   **`str`**: A color name if `color_mode` is 4 or 8
-   **`tuple[int, int, int]`**: An RGB tuple if `color_mode` is 24

**Raises:**

-   **`ColorModeError`**: If `color_mode` is invalid

---

## **colorname_to_code**

Converts a color name to its corresponding 8-bit color code. If `color` is already a valid 8-bit code (int between 0–255), it is returned as is.

```python
colorname_to_code(color: Color256)
```

**Parameters:**

-   **`color`**: A valid color name from 8-bit color system

**Returns:**

-   **`int | None`**: Returns the corresponding 8-bit color code if found, otherwise `None`

**Raises:**

-   **`None`**

---

## **code_to_colorname**

Converts an 8-bit color code to its corresponding color name. If `color` is already a valid 8-bit color name, it is returned as is.

```python
code_to_colorname(color: int)
```

**Parameters:**

-   **`color`**: A color code from the 8-bit (256-color) system

**Returns:**

-   **`str | None`**: Returns the corresponding color name if found, otherwise `None`

**Raises:**

-   **`None`**

---

## **get_all_colors**

Yields all 8-bit ANSI colors as `(name, code)` tuples. Colors can be sorted by name or code.

```python
get_all_colors(sort_by_name: bool = False)
```

**Parameters:**

-   **`sort_by_name`**: If `True`, colors will be sorted alphabetically by name. If `False` (default), colors will be sorted by their numeric code (ascending)

**Returns:**

-   **`Generator[Tuple[str, int]]`**: A generator that yields `(color_name, color_code)` pairs from the ANSI 8-bit color palette

**Raises:**

-   **`None`**

---

## **print_all_colors**

Prints all 256 colors from the **8-bit color system**, including their names and ANSI codes, sorted by ascending code order.

```python
print_all_colors()
```

---

## **search_colors**

Searches through the **8-bit** color names and yields each color that contains the provided query string in their name. Returns a generator of `(name, code)` tuples.

```python
search_colors(query: str)
```

**Parameters:**

-   **`query`**: Substring to search for within the 8-bit color names

**Returns:**

-   **`Generator[Tuple[str, int]]`**: A generator yielding `(color_name, color_code)` for matches

**Raises:**

-   **`None`**

---

## **hex_to_rgb**

Converts a hexadecimal color string to it's corresponding RGB tuple. Supports both `3` and `6` character hex codes and is case-insensitive.

```python
hex_to_rgb(hexcode: str)
```

**Parameters:**

-   **`hexcode`**: The hexadecimal color code to convert. Can be in the form `#FFF`, `FFF`, `#ffffff`, or `ffffff`

**Returns:**

-   **`Tuple[int, int, int]`**: A tuple representing the RGB color

**Raises:**

-   **`HexError`**: If the provided hexcode is not a valid hex color

---

## **rgb_to_hex**

Converts an RGB color tuple into a hexadecimal color string. Optionally includes the `#` symbol in the output.

```python
rgb_to_hex(rgb: RGBTuple, with_symbol: bool = True)
```

**Parameters:**

-   **`rgb`**: The RGB color tuple to convert
-   **`with_symbol`**: Whether to prepend the hex string with a `#`

**Returns:**

-   **`str`**: The hexadecimal color code string

**Raises:**

-   **`RGBError`**: If `rgb` is not a valid RGB tuple

---

## **is_valid_color**

Validates whether the given color is valid according to the specified color mode. Returns `True` if the color is valid, otherwise `False`.

```python
is_valid_color(color: Color, color_mode: ColorMode)
```

**Parameters:**

-   **`color`**: The color to validate
-   **`color_mode`**: The color mode of the `color`

**Returns:**

-   **`bool`**: `True` if the color is valid for the given mode, otherwise `False`

**Raises:**

-   **`None`**

---

## **is_valid_attr**

Checks if the given attribute string is a valid ANSI text style attribute.

```python
is_valid_attr(attr: Attribute)
```

**Parameters:**

-   **`attr`**: The name of the attribute to validate

**Returns:**

-   **`bool`**: `True` if the attribute is valid, otherwise `False`

**Raises:**

-   **`None`**

---

## **is_valid_hex**

Checks whether the given string is a valid hexadecimal color code. Accepts hexcodes with `3` or `6` digits, and optional `#`.

```python
is_valid_hex(hexcode: str)
```

**Parameters:**

-   **`hexcode`**: The hex color code to validate

**Returns:**

-   **`bool`**: `True` if the hexcode is valid, otherwise `False`

**Raises:**

-   **`None`**

---

## **is_valid_rgb**

Checks if the given value is a valid RGB tuple, ensuring it contains exactly three integers between `0` and `255`.

```python
is_valid_rgb(rgb: RGBTuple)
```

**Parameters:**

-   **`rgb`**: A tuple of three integers representing RGB values

**Returns:**

-   **`bool`**: `True` if the tuple is a valid RGB color, otherwise `False`

**Raises:**

-   **`None`**

---

## **Exceptions**

These below are the custom exceptions raised by `ansy`.

### **StyleError**

**Base Class:**

-   **`Exception`**

**Raised When:**

-   A style used in an ansy string is not defined in the provided style dictionary.
-   The structure or content of the style dictionary is incorrect.

**Details:**

Ensure that the style name used in the `@style_name[...]` syntax is present in the style dictionary, and that the style dictionary contains valid keys like `color_mode`, `fgcolor`, `bgcolor`, and `attrs`.

---

### **ColorModeError**

**Base Class:**

-   **`Exception`**

**Raised When:**

-   The `color_mode` value is not one of the supported modes: `4`, `8`, or `24`.

**Details:**

Ansy supports three color modes:

-   `4` for 4-bit color (16 standard colors)
-   `8` for 8-bit color (256 extended colors)
-   `24` for 24-bit color (16.7 million RGB colors)

Providing any value outside these options will raise this exception.

---

### **InvalidColorError**

**Base Class:**

-   **`Exception`**

**Raised When:**

-   A color value does not match the expected format.
-   The color name or code is not valid in **4-bit**, **8-bit**, or **24-bit** color systems.

**Details:**

This exception helps ensure that only valid colors are used across all coloring functions in Ansy.

---

### **RGBError**

**Base Class:**

-   **`InvalidColorError`**

**Raised When:**

-   The RGB value is not a tuple.
-   One or more components are not integers between `0` and `255`.
-   The tuple does not contain exactly three elements.

---

### **HexError**

**Base Class:**

-   **`InvalidColorError`**

**Raised When:**

-   The hex code contains characters outside `0-9` and `a-f/A-F`.
-   The length is not 3 or 6 (excluding the optional `#` symbol).
-   The format does not match valid hex color syntax.

---
