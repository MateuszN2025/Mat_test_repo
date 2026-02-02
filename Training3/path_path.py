from pathlib import Path
# Path("logs").mkdir(exist_ok=True)
path_to_file = "./logs/file.txt"
# Path(path_to_file).touch()
Path(path_to_file).write_text("hello")