"""Primary application entry point for the import demo project.

This module demonstrates a common larger-project pattern:

- keep executable code inside a package instead of inside a loose script
- import dependencies through a clear package namespace
- keep the top-level launcher as thin as possible
"""

import sys

# These are absolute imports from the installed package root. In larger
# projects this is often the clearest style because the origin of each
# dependency is explicit without depending on the repository folder layout.

from myapp.functions1.wrapping import wrapping
from myapp.functions2.file_funcs import fun_funcs

# To run use: python -m myapp
# What python -m myapp does:
#   Python finds the package myapp
#   Then it looks for myapp/__main__.py
#   It runs that file

@wrapping
def main():
    """Run the demo application.

    The function prints the current interpreter search path so you can observe
    where Python is looking for modules, then calls a helper imported from a
    different package submodule.
    """
    print("main")

    # Inspecting ``sys.path`` is useful in import exercises because it shows
    # exactly why some imports succeed and others fail.
    for entry in sys.path:
        print(entry)

    # This helper lives in a separate module, which makes the cross-module
    # import explicit and easy to test.
    fun_funcs()
    
main()