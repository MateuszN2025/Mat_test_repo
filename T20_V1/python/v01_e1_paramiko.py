import paramiko
import w_r

@w_r
def main():
    user = "vboxuser1"
    ip = "192.168.0.152"
    passwd = "changeme1@"

    client = paramiko.SSHClient()
    # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # client.set_missing_host_key_policy(paramiko.WarningPolicy())
    
    # in the terminal:
    #   ssh-keyscan -H 192.168.0.152 >> ~/.ssh/known_hosts
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.RejectPolicy())
    # paramiko.AutoAddPolicy() is a permissive policy that automatically
    # adds the server's host key to the client's known hosts list without
    # prompting or throwing an error. This means the connection 
    # will proceed smoothly even on first contact with a 
    # new server—the client simply accepts the key and stores it for future reference.
    try:
        client.connect(username=user, password=passwd, hostname=ip)
    except paramiko.ssh_exception.SSHException as e:
        print(f"Host key not trusted: {e}")

    stdin, stdout, stderr = client.exec_command(
        '/home/vboxuser1/calc2/b_calc - 343 898')
    output = stdout.read().decode()
    print(output)

main()


