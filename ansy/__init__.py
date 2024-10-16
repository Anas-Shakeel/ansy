""" 
## Ansy
A Python Package for Text Styling/Formatting in the terminal using
ANSI escape sequences.

"""
from __future__ import annotations

from . import exceptions
from . import colors
from .ansy import (
    make_ansi, colored, colored_gradient, make_gradient, printc,
    colored_ansy, create_style, contains_ansi,
    colored_random, get_random_color, create_random_palette,
    print_all_colors, get_all_colors, search_colors, de_ansi,
    colorname_to_code, code_to_colorname,
    hex_to_rgb, rgb_to_hex, is_valid_hex, is_valid_rgb, is_valid_attr, is_valid_color,
    COLORS_256, FGCOLORS_STANDARD, BGCOLORS_STANDARD, ANSI_REGEX,
    StandardColor, Color256, Attribute, RGBTuple, Color, ColorMode, Quality,
    ANSI_CODES, STANDARD_COLORNAMES, COLORS256_COLORNAMES, ATTRIBUTES,
)

__all__ = [
    'ANSI_CODES', 'ANSI_REGEX', 'Attribute', 'ATTRIBUTES', 'BGCOLORS_STANDARD',
    'COLORS_256', 'COLORS256_COLORNAMES',
    'Color', 'ColorMode', 'Color256', 'FGCOLORS_STANDARD', 'RGBTuple',
    'StandardColor', 'code_to_colorname',
    'colored', 'colored_ansy', 'colored_gradient', 'colored_random',
    'colorname_to_code', 'contains_ansi', 'create_random_palette', 'create_style', 
    'de_ansi', 'get_all_colors', 'get_random_color', 'hex_to_rgb',
    'is_valid_attr', 'is_valid_color',
    'is_valid_hex', 'is_valid_rgb', 'make_ansi',
    'make_gradient', 'print_all_colors', 'printc', 'Quality', 'rgb_to_hex',
    'search_colors', 'STANDARD_COLORNAMES'
]
