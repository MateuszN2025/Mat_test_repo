import shutil
from pathlib import Path
import subprocess
subprocess.run(args="clear")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")

current_file = Path(__file__)
print(f"current_file|{current_file}")
current_dir = Path(__file__).parent
print(f"current_dir|{current_dir}")
new_file = current_dir / "new_new.txt"
# new_file.touch()
new_file.write_text("Mat")
new_dir = current_dir / "new_dir"
new_dir222 = current_dir / "new_dir222"
# new_dir.mkdir()
shutil.copy(new_file,new_dir222)
print("------------------------------------------")
for dir in current_dir.iterdir():
    print(str(dir).rsplit("/")[7])
print("------------------------------------------")
for dir in current_dir.glob("*.py"):
    print(str(dir).rsplit("/")[7])
# *.py = anything ending in .py
# .py = file named only .py
# shutil.move(new_dir222, new_dir)
new_new_2 = new_dir / "new_dir222" / "new_new.txt"

print(new_new_2)
if new_new_2.is_file():
    new_new_2.unlink()
else:
    print("FILE DOES NOT EXIST⚠️")
    
print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303
