import subprocess

def execute_command(path:str, b_script:str, oper:str, a:str, b:str):
    # b_calc + 34 34
    cmd = subprocess.run(args=[path + b_script,
                               oper,
                               a,
                               b],
                         capture_output=True,
                         text=True,
                         check=True
                         )
    return cmd.stdout

path = "/home/mniedziolka/PP/Mat_test_repo/T10/application/"
b_script = "b_calc"
oper = "+"
a = "343"
b = "898"

r = execute_command(path, b_script, oper, a, b)
print(r, end="")