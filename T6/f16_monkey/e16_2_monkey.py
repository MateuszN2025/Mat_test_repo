import sys
from folder_funcs import file_funcs as f

from T0.wrapping import wraping as w
@w
def main():
    
    print("main")
    for _ in sys.path:
        # print(_) if "T6" in _ else None
        print(_)
    f.fun_funcs()

main()

"""# export PYTHONPATH=/home/mniedziolka/PP/Mat_test_repo"""

# PYTHONPATH=/home/mniedziolka/PP/Mat_test_repo  <python interpreter>  <script to run>

# python some_file.py
#   means “run this file by path”

# python -m package.subpackage.module
#   means “run this module by import name”

# python /path/to/e16_2_monkey.py
# python -m T6.f16_monkey.e16_2_monkey

# -m tells Python:
#   “Do not run a file by path. Run a module by its import name.”

# python file.py = “open this file directly”
# python -m package.module = “import this module and run it as

# Python treats Mat_test_repo as the import root, so both of these can be found:
#   T6.f16_monkey.e16_2_monkey
#   T0.wrapping