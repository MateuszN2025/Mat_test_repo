import rest_api_func_e as res
import subprocess
import json
from pathlib import Path
subprocess.run(args="clear")

current_dir = Path(__file__).resolve().parent

print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")

def main():
    p1 = res.Pokemon("ditto")
    file_path = f"{current_dir}/8_poke.json"
    with open(file_path, "w") as file:
        json.dump(obj=p1.get_poke_info(), fp=file, indent=4)
        
    # print(isinstance(True, int))

if __name__ == "__main__":
    main()

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303
