# Ansy

[![Automated testing results](https://img.shields.io/github/actions/workflow/status/anas-shakeel/ansy/.github/workflows/python-package.yml?branch=main)](https://github.com/anas-shakeel/ansy/actions/workflows/python-package.yml?query=branch%3Amain)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Latest PyPi version](https://img.shields.io/pypi/v/ansy.svg)](https://pypi.python.org/pypi/ansy)
[![PyPI downloads](https://static.pepy.tech/badge/ansy/month)](https://pypi.org/project/ansy/)<br/>
[![Project licence](https://img.shields.io/pypi/l/ansy?color=blue)](https://github.com/Anas-Shakeel/ansy/blob/main/LICENSE)
[![supported Python versions](https://img.shields.io/pypi/pyversions/ansy)](https://pypi.python.org/pypi/ansy)

`ansy` (_pronounced ANSI_) is a lightweight yet powerful Python library designed to supercharge your command-line output with vivid, expressive styling.

Ansy helps you add colors and styles to your terminal output. It is made for developers who want their CLI apps to look clean, colorful, and easy to read without using heavy libraries or writing complex code.

!!! note ""
    Ansy was inspired by the [`termcolor`](https://github.com/termcolor/termcolor) module. Anything that **termcolor** can do, **ansy** can do it too... _and more!_

## **Why use Ansy?**

-   **Multiple Color Modes** — You can color your text using `4-bit`, `8-bit`, or `24-bit` (**RGB**) color modes. It works on most modern terminals. _(Some older terminals may only support `4-bit` colors)_ [Learn more](usage.md#choosing-color-modes)
-   **Style Just What You Need** — You don’t have to color the whole string. Ansy lets you color just parts of a string, like a word, a number, or a keyword. [Learn more](usage.md#coloring-parts-of-a-string)
-   **Gradients & Random Colors** — Want your text to pop? You can apply smooth gradients or even use random colors to make your output stand out. [Learn more](usage.md#applying-gradients)
-   **Text Formatting** — Make your output easier to read with **bold**, _italic_, <u>underline</u>, and more formatting options built right in.
-   **Remove Styling When Needed** — Ansy can strip away all colors and styles, giving you clean, plain text when needed. For example, when logging or saving to a file. [Learn more](usage.md#removing-ansi-escape-codes)
-   **Common Colors Built In** — No need to search for color codes. Ansy gives you easy access to commonly used colors with clear names and hex codes. [Learn more](usage.md#the-colors-module)
-   **Zero Dependencies** — Written in pure Python, Ansy has no third-party dependencies, making it reliable, portable, and easy to integrate into any project.
-   **Developer-Friendly API** — The code is easy to write and easy to understand. You don’t need to learn anything complicated to use Ansy.
-   **Very Lightweight** — The whole library is under **90 KB**, and most of that is helpful stuff like _docstrings_, _color data_, and _type hints_ for better code. Ansy stays lean without sacrificing power.

---

## *Preview*

![A preview of Ansy in action](https://raw.githubusercontent.com/Anas-Shakeel/ansy/refs/heads/main/docs/images/demo.gif)