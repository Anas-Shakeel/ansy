# Usage

`ansy` was meant to be simple and easy to use, so it should not give you a hard time. _(If it does, Then Uninstall it right away!)_

## **From Termcolor to Ansy**

If your code uses `termcolor` and you want to shift to `ansy`, you can safely replace the `colored` function of `termcolor` with the `colored` function of `ansy`.

=== "ansy"

    ``` py
    from ansy import colored

    colored(
      text='this is ansy',
      fgcolor='light_red',
      bgcolor='dark_grey',
      attrs=['bold']
    )
    ```

=== "termcolor"

    ``` py
    from termcolor import colored

    colored(
      text='this is termcolor',
      color='light_red',
      on_color='dark_grey',
      attrs=['bold']
    )
    ```

???+ Warning
    Make sure to change argument name `color` to `fgcolor` & `on_color` to `bgcolor` if you were using keyword arguments. And also change the bgcolor name from `on_x` to just `x`. (e.g `on_red` to `red`)

---

## **Coloring a String**

Use the [`colored`](./api-reference/ansy.md#colored) function, if you want to colorize a string.
Easily apply **ANSI** colors and text attributes to your strings using the `colored` function:

```py
from ansy import colored

# Bold red text on a white background
red_white = colored(
    text="This is a string",
    fgcolor="red",
    bgcolor="white",
    attrs=["bold"]
)
print(red_white)
```

![Output Example Image](https://raw.githubusercontent.com/Anas-Shakeel/ansy/main/docs/images/colored_str 1.png){ loading=lazy }

???+ tip
    Leave any argument as `None` (or omit) to simply skips that formatting layer.


### Quick Print

If you just want to print a colored string without storing it, [`printc()`](./api-reference/ansy.md#printc) is your friend:

```py
from ansy import printc

printc(
    "Print this string after formatting.",
    fgcolor="plum",
    attrs=["italic"],
    color_mode=8
)
```

![Output Example Image](https://raw.githubusercontent.com/Anas-Shakeel/ansy/main/docs/images/colored_str 7.png){ loading=lazy }

`printc()` is just `colored()` function with auto-print feature (and no return!). So use it as you would use `colored()` (without return, ofcourse 😉)

### Choosing Color Modes

The `color_mode` parameter lets you pick between:

-   **4-bit** (16 colors)
-   **8-bit** (256 colors)
-   **24-bit** (truecolor, ~16.7M colors)

```py hl_lines="4 5"
# Underlined Text with brown_sandy FG and grey_9 BG.
printc(
    "This is a string",
    fgcolor=215, # brown_sandy
    bgcolor=240, # grey_9
    attrs=["underline"],
    color_mode=8,
)
```

Notice i've also changed the colors to some codes. These codes belong to the `8-bit` color system and they range from `0` to `255`. Refer to this [256 color chart](https://upload.wikimedia.org/wikipedia/commons/1/15/Xterm_256color_chart.svg).

You can pass either color codes or human-friendly names:

```py hl_lines="4 5"
# Same Underlined Text with brown_sandy FG and grey_9 BG.
printc(
    "This is a string",
    fgcolor="brown_sandy",
    bgcolor="grey_9",
    attrs=["underline"],
    color_mode=8
)

```

![Output Example Image](https://raw.githubusercontent.com/Anas-Shakeel/ansy/main/docs/images/colored_str 3.png){ loading=lazy }

To explore all available 8-bit colors, use [`get_all_colors()`](./api-reference/ansy.md#get_all_colors). It yields a tuple containing color name and code on each iteration.

```py
from ansy import get_all_colors

# Print all 256 colors
for name, code in get_all_colors():
    print(f"{code}: {name}")

```

Or just call [`print_all_colors()`](./api-reference/ansy.md#print_all_colors).

```py
from ansy import print_all_colors

print_all_colors()
```

### Truecolor Support

Most Modern terminals support **RGB** or **Truecolor** which offer a much much more wider range of colors _(approx. **16.7 million** colors)_.

`24-bit` color system accepts **RGB** tuple as well as **Hex** color codes.

```py
# RGB tuple
fg = (255, 100, 100)
bg = (215, 215, 215)
printc("This is a string", fg, bg, ["italic"], color_mode=24)

# Hex codes
printc("This is a string", "#FF6464", "#D7D7D7", ["italic"], color_mode=24)
```

![Output Example Image](https://raw.githubusercontent.com/Anas-Shakeel/ansy/main/docs/images/colored_str 6.png){ loading=lazy }

---

## **Coloring Parts of a String**

By default, [`colored()`](./api-reference/ansy.md#colored) applies formatting to the **entire** string you pass in. But what if you want to apply different styles to specific **parts of a string?**

Let’s start with the basic way to do that:

```py
from ansy import colored

# Format only the word "World"
formatted_world = colored('World', fgcolor='purple', attrs=['bold'], color_mode=8)
print(f"Hello, {formatted_world}!")
```

![Output Example Image](https://raw.githubusercontent.com/Anas-Shakeel/ansy/main/docs/images/colored_selective 1.png){ loading=lazy }

Want to style **"Hello"** differently too?

```py
formatted_hello = colored('Hello', fgcolor='orange', color_mode=8)
formatted_world = colored('World', fgcolor='purple', attrs=['bold'], color_mode=8)

print(f"{formatted_hello}, {formatted_world}")
```

![Output Example Image](https://raw.githubusercontent.com/Anas-Shakeel/ansy/main/docs/images/colored_selective 2.png){ loading=lazy }

That works, but as you can imagine, this gets messy quickly in larger strings.

The solution to this problem is [`colored_ansy()`](./api-reference/ansy.md#colored_ansy) function. It adds the styling defined in `style` dictionary to wherever an **Ansy string** is found in the whole string.

### Ansy Strings

An _Ansy string_ is a special inline markup format:

```
@style_name[Your text here]
```

!!! info "Syntax of an Ansy String"
    An **Ansy String** starts with `@` symbol followed by the name of the style (defined by the `style` dictionary), and the text in backets `[text]` to which you want to apply the formatting.
    ```py
    ansy_string = "This is @my_style[your text]"
    ```

You define the styles (_presets_) separately in a **style dictionary**, and `colored_ansy()` applies them wherever it finds these tags.

### Style Dictionary

**Style dictionary** is a dictionary which defines the style(s) to apply to the ansy strings. Each `style` is a dictionary describing **how to format** the text:

```py
style = {
    "my_style": {
        "color_mode": 8,
        "fgcolor": "light_red",
        "bgcolor": 255,
        "attrs": ["bold", "italic"]
    }
}
```

Purpose of this structure is so that you could define all your styles in one dictionary and then use it everywhere, instead of creating a dictionary for each style and create a mess in your code.

!!! note
    Name of the style dictionary doesn't have to be `style`.

Every key in this `style` dictionary is the name of the style that you're gonna use in the `ansy strings`.

Each style must have 4 `key:value` pairs:

-   `color_mode`: Choose from `4`, `8`, or `24`
-   `fgcolor`: Foreground color (name, code, RGB, or Hex)
-   `bgcolor`: Background color
-   `attrs`: List of attributes, like `bold`, `italic`, `underline` etc

!!! note
    `color_mode` decides which colors to use and you should only provide colors supported by that mode. 

Now, Back to our problem.

```py
from ansy import colored_ansy

style = {
    "orange": {
        "color_mode": 8,
        "fgcolor": "orange",
        "bgcolor": None,
        "attrs": None
    },
    "purple": {
        "color_mode": 8,
        "fgcolor": "purple",
        "bgcolor": None,
        "attrs": ["bold"]
    }
}

formatted = colored_ansy("@orange[Hello] @purple[World]", style)
print(formatted)

```

![Output Example Image](https://raw.githubusercontent.com/Anas-Shakeel/ansy/main/docs/images/colored_selective 2.png){ loading=lazy }

You must be thinking, **Wow! Nicely Simplified. We now have to write even more lines of code**, right?

Well yeah! but only if you do it manually. There is another function called [`create_style()`](./api-reference/ansy.md#create_style) which makes it easier to define styles. _(Yup! there's a function for everything)_

```py
from ansy import colored_ansy, create_style

# Create styles
style = {
        "orange": create_style(8, 'orange'),
        "purple": create_style(8, 'purple', attrs=['bold'])
}

formatted = colored_ansy("@orange[Hello] @purple[World]", style)
print(formatted)
```

![Output Example Image](https://raw.githubusercontent.com/Anas-Shakeel/ansy/main/docs/images/colored_selective 2.png){ loading=lazy }

Still more code, but it's just a one time thing! now you can use `orange` and `purple` style to format as many parts as you want.


### Example

This below example hides some parts of text using `concealed` [attribute](./useful-to-know.md#attributes).

```py
# Reusing style Dictionary
style['hide'] = create_style(attrs=['concealed'])

formatted = colored_ansy(
    'Hide this @hide[..], & this @hide[++], but not this @hide[**]',
    style
)

print(formatted)

```

![Output Example Image](https://raw.githubusercontent.com/Anas-Shakeel/ansy/main/docs/images/colored_selective 3.png){ loading=lazy }

!!! note
    `concealed` doesn’t delete text. It just makes it invisible in the terminal. _(you can confirm this by copying the hidden area and pasting it into your text editor)_

---

## **Applying Gradients**

**Ansy** lets you apply horizontal gradients to the foreground of your strings using the [`colored_gradient()`](./api-reference/ansy.md#colored_gradient) function.

```py
from ansy import colored_gradient

# Smooth gradient from red to blue (left to right)
formatted = colored_gradient("This is ansy.", (255, 100, 100), (100, 50, 200))
print(formatted)
```

![Output Example Image](https://raw.githubusercontent.com/Anas-Shakeel/ansy/main/docs/images/colored_gradient 1.png){ loading=lazy }

???+ warning
    Gradients are only available in **24-bit** color mode. So make sure your terminal supports it.


### Faking Vertical Gradient 

[`colored_gradient()`](./api-reference/ansy.md#colored_gradient) only supports horizontal gradients. But with a clever trick, you can simulate **vertical gradients** by using line breaks (`\n`) in your string:

```py
text = (
    "This text is\n"
    "going to be used\n"
    "to create or fake\n"
    "a vertical gradient."
)
print(colored_gradient(text, "#00ffff", "#b00b1e"))
```

![Output Example Image](https://raw.githubusercontent.com/Anas-Shakeel/ansy/main/docs/images/colored_gradient 2.png){ loading=lazy }

Technically, it's still a horizontal gradient, but each line starts a bit deeper into the gradient transition, giving it a **diagonal** or **vertical illusion**.

---

## **Random Colors**

**Ansy** can randomly colorize your strings. Just for fun, experimentation, or creating playful terminal UIs.

```py
from ansy import colored_random

formatted = colored_random("Random Random, Evil Phantom!")
print(formatted)
```

![Output Example Image](https://raw.githubusercontent.com/Anas-Shakeel/ansy/main/docs/images/colored_random 1.png){ loading=lazy }


!!! note
    By default, [`colored_random()`](./api-reference/ansy.md#colored_random) picks a random color from the `4-bit` colorsystem and applies it to the entire string. But you can go much further.


### Target Based Randomization

You can control how randomness is applied by choosing a `target`:

```py
print(colored_random('Apply random colors to each word', target='words'))
print(colored_random('Apply random colors to each character', target='chars'))
```

![Output Example Image](https://raw.githubusercontent.com/Anas-Shakeel/ansy/main/docs/images/colored_random 2.png){ loading=lazy }

???+ warning
    While `target="chars"` lets you apply random colors to each individual character, **it's not recommended** with the `24-bit` color mode especially for longer strings.

    [**ANSI escape codes**](https://en.wikipedia.org/wiki/ANSI_escape_code) (used for styling terminal output) are added before and after each character. In `24-bit` mode, these codes are much longer because they include full **RGB** values.

    For example, formatting `"This"` with `24-bit` mode and `target="chars"`:
    ```py
    colored_random("This", target="chars", color_mode=24)
    ```

    might generate something like:
    ```py
    '\x1b[38;2;5;155;190mT\x1b[0m\x1b[38;2;119;11;99mh\x1b[0m\x1b[38;2;24;50;220mi\x1b[0m\x1b[38;2;178;45;244ms\x1b[0m'
    ```
    That's over **100** characters just to render **4**!

    So for longer strings, this quickly becomes **inefficient** and **bloats the output**.

**Recommended:**

-    Prefer `target="words"` or `target="all"` when using `color_mode=24`
-    If you must color per character, consider using `8-bit` mode (`color_mode=8`) for a lighter output


### Custom Color Palettes

You can use a **custom palette** to avoid **completely random chaos** and keep things visually consistent.

```py
# Palette of 24-bit colors
palette = ["#69D2E7", "#A7DBD8", "#E0E4CC", "#F38630", "#FA6900"]

formatted = colored_random(
    "Not so random palette.",
    custom_palette=palette,
    target="words",
    color_mode=24
)

print(formatted)
```

![Output Example Image](https://raw.githubusercontent.com/Anas-Shakeel/ansy/main/docs/images/colored_random 3.png){ loading=lazy }

!!! note
    You can use colors from any color system (**Name**, **Code**, **Hex**, or **RGB**). Just make sure to set the appropriate `color_mode`.

---

## **Removing ANSI Escape Codes**

Sometimes, you might want to **strip out all styling** and get back the plain, unformatted version of a string. Especially if you're **logging output**, **comparing values**, or **writing to a file.**

**Ansy** provides the handy [`de_ansi()`](./api-reference/ansy.md#de_ansi) function just for that!

```py
from ansy import colored, de_ansi

ansi_string = colored(
    "This string contains ANSI",
    fgcolor="light_blue",
    bgcolor="dark_grey",
    attrs=["italic"]
)
clean_string = de_ansi(ansi_string)

print([ansi_string])
print([clean_string])
```

![Output Example Image](https://raw.githubusercontent.com/Anas-Shakeel/ansy/main/docs/images/deansi 1.png){ loading=lazy }


!!! tip
    If you ever want to check whether a string contains ansi codes, just print it like a list `print([ansi_string])`. That way, **ANSI escape codes** won't escape **(No Pun Intended)**

## **The Colors Module**

Ansy ships with a beautiful, ready-to-use **24-bit color collection**. Inspired by popular design systems and palettes.

It includes:

-   [**Material Colors**](./useful-to-know.md#material-colors) (**19** base colors × **14** shades each)
-   [**Web/HTML Colors**](./useful-to-know.md#html-or-web-colors) (**140** standard named colors)
-   **Color Palettes** (**200** colors with **5** colors in each palette)


All of these are accessible via the [`colors`](./api-reference/colors.md) module:

```py
from ansy import colors
```

### Material Colors

Get all shades of a color from **Material Colors** using [`get_material_color()`](./api-reference/colors.md#get_material_color):

```py
red_shades = colors.get_material_color("red")
print(red_shades)
```

### HTML or Web Colors

Get **HTML or Web Colors** using [`get_web_colors()`](./api-reference/colors.md#get_web_colors). It returns a generator iterator, which yields dictionaries of colors from **HTML or Web Colors**.

```py
for color_dict in colors.get_web_colors():
    print(color_dict)
```

### Color Palettes

Get **Predefined Color Palettes** using [`get_palettes()`](./api-reference/colors.md#get_palettes). It returns a generator iterator, which yields a list of colors _(a palette)_ on each iteration.

```py
for palette in colors.get_palettes():
    print(palette)
```

These color utilities are especially useful when working with [`colored_random()`](./api-reference/ansy.md#colored_random), **defining themes**, or just exploring visually cohesive color schemes for CLI applications.
