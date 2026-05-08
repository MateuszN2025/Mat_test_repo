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
        file = "bash1.sh"
        with open(file, "w") as b:
            b.write(result)
                    
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
    return bash_script
    
main()
    
