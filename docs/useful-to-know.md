# Useful To Know

## **Attributes**

There are several attributes in `ansy` but not all are widely supported. Some may not work as expected or not work at all.

| Attribute          | What it does                                                      | Widely Supported |
| :----------------- | ----------------------------------------------------------------- | :--------------- |
| `bold`             | bolds the text or increases intensity                             | ✅               |
| `dark`             | Darkens the text                                                  | ✅               |
| `italic`           | Italicizes the text                                               | ❌               |
| `blink`            | Sets the blinking to less than 150 times per minute               | ❌               |
| `reverse`          | Swaps foreground and background colors of text                    | ✅               |
| `concealed`        | Hides the text visually, but does not remove                      | ❌               |
| `underline`        | Underlines the text                                               | ✅               |
| `double-underline` | Double-Underlines the text (Disables bold mode on some terminals) | ✅               |
| `overline`         | Overlines the text i.e line above the text                        | ❌               |
| `strike`           | Strikes the text, as if marked for deletion                       | ❌               |

## **Standard Colors (4-Bit)**

`black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`,

`light_grey`, `dark_grey`, `light_red`, `light_green`, `light_yellow`,

`light_blue`, `light_magenta`, `light_cyan`

## **256 Colors (8-Bit)**

Refer to [256 colors cheat sheet](https://www.ditig.com/256-colors-cheat-sheet) for color names and codes. _(color names in `ansy` have been updated but codes remain the same)_

You can also call `ansy.print_all_colors()` to see all color names and their codes.

## **HTML or Web Colors**

Refer to this resource for [HTML Colors](https://materialui.co/htmlcolors).

## **Material Colors**

These below are the names of **Material Colors.**

`red`, `pink`, `purple`, `deeppurple`, `indigo`, `blue`, `lightblue`,

`cyan`, `teal`, `green`, `lightgreen`, `lime`, `yellow`, `amber`,

`orange`, `deeporange`, `brown`, `grey`, `bluegrey`.

These below are the shades of each **Material Color.**

`50`, `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900`,

`a100`, `a200`, `a400`, `a700`.

Refer to this [Material Colors](https://materialui.co/colors) chart.
