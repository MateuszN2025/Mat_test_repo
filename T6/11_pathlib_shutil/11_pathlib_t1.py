from pathlib import Path
import shutil

import subprocess
subprocess.run(args="clear")

print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")

# Base paths
current_dir = Path(__file__).resolve().parent
"""
resolve
    Make the path absolute, resolving all symlinks on the way and also
    normalizing it (for example turning slashes into backslashes under
    Windows).
"""

print(f"{__file__}")
print(f"{type(__file__)}")
current_file = Path(__file__)
print(f"{type(current_file)}")

current_dir = current_file.parent
project_root = current_dir.parent

print("------------------------------------------")
print(f"Current file: {current_file}")
print(f"Current dir : {current_dir}")
print(f"Project root: {project_root}")
print("------------------------------------------")

# Build paths
file_path = current_dir / "example.txt" 
# Because current_dir is not a normal string. It is a Path object from pathlib.
# Path objects redefine the / operator so it means “join paths”, not division.

print(f"{file_path}")
open(file_path, "w")

# json_path = current_dir / "data" / "config.json"
new_dir = current_dir / "temp_folder2"

# # Create directory
new_dir.mkdir(parents=True, exist_ok=True)


# # Check existence / type
print("-----------------Check existence / type-------------------------")
print(file_path.exists())      # True / False
print(file_path.is_file())     # True / False
print(new_dir.is_dir())        # True / False

# Create / write file
file_path.write_text("Hello from pathlib\n", encoding="utf-8")

# Append to file
with file_path.open("a", encoding="utf-8") as f:
    f.write("Another line\n")

# Read file
print("---------------Read file---------------------------")
content = file_path.read_text(encoding="utf-8")
print(content)

# Read lines
print("---------------Read lines---------------------------")
lines = file_path.read_text(encoding="utf-8").splitlines()
print(lines)

# File info
print("----------------File info--------------------------")
print(f"current_dir: ", current_dir)          # example.txt
print(f"file_path.name: ", file_path.name)          # example.txt
print(f"file_path.stem: ", file_path.stem)          # example
print(f"file_path.suffix: ", file_path.suffix)        # .txt
print(f"file_path.parent: ", file_path.parent)        # parent folder
print(f"file_path.absolute(): ", file_path.absolute())    # absolute path

# Rename file
print("----------------Rename file--------------------------")
renamed_file = current_dir / "renamed_example.txt"
file_path.rename(renamed_file)

# Copy file
print("-----------------Copy file-------------------------")
copied_file = current_dir / "copy_example.txt"
shutil.copy(renamed_file, copied_file)

# # Delete file
# if copied_file.exists():
#     copied_file.unlink()

# List files in directory
print("---------------List files in directory---------------------------")
for item in current_dir.iterdir():
    print(item)

# Find files by pattern
print("----------------Find files by pattern--------------------------")
for txt_file in current_dir.glob("*.txt"):
    print(f"TXT: {txt_file}")

# Recursive search
print("----------------Recursive search--------------------------")
for py_file in current_dir.rglob("*.py"):
    print(f"PY: {py_file}")

# # Safe open for reading
# if renamed_file.exists():
#     with renamed_file.open("r", encoding="utf-8") as f:
#         print(f.read())

# # Remove empty directory
# empty_dir = current_dir / "empty_folder"
# empty_dir.mkdir(exist_ok=True)
# empty_dir.rmdir()

# # Remove directory tree
# dir_to_remove = current_dir / "temp_to_delete"
# dir_to_remove.mkdir(exist_ok=True)
# (dir_to_remove / "a.txt").write_text("temp", encoding="utf-8")
# shutil.rmtree(dir_to_remove, ignore_errors=True)

"""
pathlib:
file_path.exists()
file_path.rename(new_path)
file_path.unlink()
file_path.read_text()

shutil:
shutil.copy(src, dst)
shutil.copy2(src, dst)
shutil.move(src, dst)
shutil.rmtree(folder)
"""



print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303



