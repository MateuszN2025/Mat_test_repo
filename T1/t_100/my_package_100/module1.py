from submodules import submodule1
from submodules.submodule1 import bbb


if __name__ == "__main__":
    submodule1.aaa()
    bbb()
    print(__name__)

"""
if __name__ == "__main__":
    # run this only if the file is executed
This lets the file do two jobs:

1️⃣   Act as a program
2️⃣   Act as a library

| Situation               | What is `__name__`? |
| ----------------------- | ------------------- |
| You **run** the file    | `"__main__"`        |
| You **import** the file | The file's name     |

"""


