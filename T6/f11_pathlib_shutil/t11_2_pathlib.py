from pathlib import Path
import shutil

import subprocess
subprocess.run(args="clear")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")


print("------------------------------------------")
current_file_path = Path(__file__)
print(f"current_file_path: {current_file_path}")
print("------------------------------------------")
current_dir = current_file_path.parent
print(f"current_dir: {current_dir}")
print("------------------------------------------")
new_file = current_dir / "new_file.txt"
print(f"new_file: {new_file}")
print("------------------------------------------")
new_file.write_text("new file")
# new_file3 = current_dir / "new_file3.txt"
# new_file3.touch(exist_ok=False) # exist_ok=False - prevent from creation the same file
print("------------------------------------------")
# new_file_in_dir = current_dir / "new_folder/new_file4.txt" # ❌ first you need to create a dir
# print(new_file_in_dir)
# new_file_in_dir.touch()
new_file5 = current_dir / "new_file5.txt"
new_file5.touch()
print("------------------------------------------")
new_dir = current_dir / "new_dir"
new_dir.mkdir(exist_ok=True)
new_file_in_new_dir = new_dir / "new_file_in_dir.txt"
print(new_file_in_new_dir)
new_file_in_new_dir.touch()








print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303

