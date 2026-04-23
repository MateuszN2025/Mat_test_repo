from pathlib import Path
import shutil
import subprocess
from datetime import datetime

subprocess.run(args="clear")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")



path_to_file = Path(__file__)
print(f"{path_to_file}")
path_to_dir = Path(__file__).parent
print(f"{path_to_dir}")
new_file = path_to_dir / "exam.txt"
new_file.touch()

info = new_file.stat()
print(f"name: {new_file.name}")
print(f"path: {new_file}")
print(f"size: {info.st_size} bytes")
print(f"last access: {datetime.fromtimestamp(info.st_atime)}")
print(f"last modified: {datetime.fromtimestamp(info.st_mtime)}")
print(f"metadata changed: {datetime.fromtimestamp(info.st_ctime)}")


# birth_time = getattr(info, "st_birthtime", None)

# if birth_time is not None:
#     print(f"created: {datetime.fromtimestamp(birth_time)}")
# else:
#     print("creation date is not available from Python on this platform")

list1 = [str(i)+"\n" for i in range(5)]
# for item in list1:
# f.write(f"{item}\n")
print(f"{list1}")
# [new_file.write_text(str(item)) for item in list1]
with new_file.open("a", encoding="utf-8") as f:
    # for item in list1:
    f.writelines(list1)
    # f.write(list1) # TypeError: write() argument must be str, not list
    chars = f.write("string")

print(chars)

# new_file.rename("aaa")
new_path = Path("/home/mniedziolka/PP/")
print(new_path)
aaa_file = new_path / "aaa.txt"
print(aaa_file)
# aaa_file.write_text("aaa")
# aaa_file.rename(path_to_dir / "bbb")
# shutil.copy(path_to_dir / "bbb", path_to_dir / "ccc.txt")
# ccc = path_to_dir / "ccc.txt"
bbb = path_to_dir / "bbb"
if bbb.is_file():
    bbb.unlink()
else:
    print(f"File does not exist")
    
new_folder = path_to_dir / "new_folder"
# new_folder.mkdir()
# shutil.move(new_file, new_folder)
print("------------------------------------------")
import re
# r = r"/*."
# pattern = r"^...$"
# text = "your text"
# match = re.match(pattern, text)
# if match:
#     print("matched")
# else:
#     print("no match")

pattern = r"///////*.*"

# for item in path_to_dir.iterdir():
#     # match = re.match(pattern, str(item))
#     # if match:
#     #     print(match.group(0))
#     print(str(item).strip())

string = "   sadkalsjd /kjasdlksj   "
print(string)
print(string.strip())
print(string.rsplit("/"))

print("------------------------------------------")
for item in path_to_dir.iterdir():
    print(str(item).rsplit("/")[7])
print("------------------------------------------")
for item in path_to_dir.glob("*.py"):
    print(f"item: {str(item).rsplit('/')[7]}")
















print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303
