import subprocess
import w_r

user = "vboxuser1"
ip = "192.168.0.152"
passwd = "changeme1@"

command = ["sshpass", "-p", passwd, "ssh", f"{user}@{ip}", '/home/vboxuser1/calc2/b_calc', '-', '343', '898']

@w_r
def main():
    result = subprocess.run(args=command)
    print(result.stdout)
    
main()