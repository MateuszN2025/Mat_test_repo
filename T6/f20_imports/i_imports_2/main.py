from func11 import func11
from func22.func22 import func22
import w_r
import sys
from pathlib import Path

# root_dir = Path(__file__).resolve().parents[3]
# sys.path.insert(0, str(root_dir)) # ⚠️ str() !!!

# export PYTHONPATH=/home/mniedziolka/PP/Mat_test_repo/

from T0.wrapping import wraping
from T6.T0.wrapping2 import wraping2

@w_r
@wraping
@wraping2
def main():
    func11()
    func22()
    print("------------------------------------------")
    [print(_) for _ in sys.path]
    
main()