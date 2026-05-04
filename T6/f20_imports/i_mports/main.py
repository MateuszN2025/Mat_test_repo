from f1 import hi as h
from fun.f2 import hi5 as h5
import w_r

import sys
from pathlib import Path

# sys.path.append(Path(__file__).resolve())


PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from T0.wrapping import wraping
from T6.T0.wrapping2 import wraping2

@w_r
@wraping
@wraping2
def main():
    # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # print(Path(__file__).resolve())
    # p = Path(__file__).resolve()
    # print(p.parent)
    # print(p.parents[2])
    # print(p.parents[3])
    # print(type(p.parent))
    # print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    
    
    print("------------------------------------------")
    [print(path) for path in sys.path]
    print("------------------------------------------")
    h()
    h5()
    
    # export PYTHONPATH="/home/.../Mat_test_repo/T0" ℹ️
    
    
if __name__ == "__main__":
    main()
    """
    When you do import T0.wrapping Python looks for a 
    directory named T0 inside each path in sys.path.
    export PYTHONPATH="/home/.../Mat_test_repo" puts Mat_test_repo on sys.path, 
    so Python finds wrapping.py and import T0.wrapping works.
    
    export PYTHONPATH="/home/.../Mat_test_repo/T0" puts the 
    T0 directory itself on sys.path. Python will then try
    to find T0 inside that entry (i.e. .../T0/T0⚠️), which doesn’t exist
    — hence the ModuleNotFoundError.
    """
    