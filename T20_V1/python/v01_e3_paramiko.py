import paramiko


def main() -> None:
    user = "vboxuser1"
    ip = "192.168.0.152"
    passwd = "changeme1@"
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.RejectPolicy())
    
    try:
        client.connect(hostname=ip, username=user, password=passwd, timeout=5)
        stdin, stdout, stderr = client.exec_command("id")
        output = stdout.read().decode().strip()
        
        # without strip: ⚠️
        # The ? line with + at the end means main() returns
        # the string with a trailing newline
        # (\n) or space. SSH command output almost always ends with \n.
        # E         Skipping 79 identical leading characters in diff, use -v to show
        # E         - (vboxusers)       
        # E         + (vboxusers)
        # E         ?            +
        
        print(output)
    except paramiko.ssh_exception.SSHException as e:
        print(f"⚠️ Host key not trusted: {e}")
        
    client.close()
    return output
    
main()
    