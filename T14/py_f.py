# import sys

# print(sys.argv)
# print("script name:", sys.argv[0])
# print("first arg:", sys.argv[1])
# print("second arg:", sys.argv[2])


# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("--name")
# parser.add_argument("--age", type=int)

# args = parser.parse_args()

# print(args.name)
# print(args.age)
import subprocess
import w_r

def basher(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  
        
        # print("------------------------------------------")
        # print(result)
        # print("------------------------------------------")
        
        file = "bash1.sh"
        with open(file, "w") as b:
            b.write(result)
        # "bash1.sh" works because you create and use it in the current directory.
        # For files that already exist (like py_file_input.py), you must specify 
        # the correct relative path from where you run the script, or ensure you
        # always run the script from the directory where the file is located.
                    
        output = subprocess.run(["bash", f"./{file}"],
                       capture_output=True,
                       text=True,
                       check=True)
        print("--- BASH SCRIPT---")
        print(result)
        print("---   OUTPUT   ---\n")
        print(output.stdout)
      
    return wrapper

@w_r
@basher
def main():
    bash_script="""
    
    date +%F 
    
    """
    pyfile = "T14/py_file_input.py"
    bash_script2 = ""
    with open(pyfile, "r") as f:
        for line in f:
            if line.strip().startswith("'''") or line.strip().startswith('"""'):
                continue
            bash_script2 += line
    
    # print(type(bash_script2))
    # print("------------------------------------------")
    # print(bash_script2)
    
    return bash_script2
    
main()
    
