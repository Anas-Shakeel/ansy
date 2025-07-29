# **Installation**

Ansy is available on **PyPI** and can be installed with `pip`.

```bash
pip install ansy
```

This installs the latest version from [PyPI](https://pypi.org/project/ansy). If you've got **Python 3.8+** and `pip` installed, you're good to go. [See also](./compatibility.md)

## **Quick Check**

To verify the installation, run `ansy` alone or with `-h` flag in the terminal:

```sh
ansy -h
```

You should see help text from ansy!

## **Example Usage**

Here’s a minimal example that prints colored text onto the terminal:

```py
from ansy import printc

printc("The background is red!", bgcolor="red")
```

## **Windows Console Support**

**Ansy** has zero dependencies, but if you're on **Windows**, you may need to install [`colorama`](https://pypi.org/project/colorama/) to enable proper color rendering in the _Command Prompt_ or _PowerShell_.

**Install colorama (only on Windows)**

```bash
pip install colorama
```

Then initialize it in your script before using ansy:

```py
from ansy import printc
from colorama import just_fix_windows_console

just_fix_windows_console()
printc("The background is red!", bgcolor="red")
```

This ensures that **ANSI escape codes** display correctly on Windows terminals.

!!! note 
    This step is only needed on **Windows**. On **Linux** and **MacOS**, ansy works out of the box.
