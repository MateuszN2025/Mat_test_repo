# __init__.py
# mark a directory as a Python package.
# it lets Python treat the folder as importable
# package/module structure
# it enables package-relative imports like:
#   from .helpers import execute_command
# 
# Without it, Python may treat the folder as just a plain directory,
# and imports can break depending on how pytest is run.