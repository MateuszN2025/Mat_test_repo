import subprocess

class Basher:

    def __init__(self, user, password, ip):
        self.user = user
        self.password = password
        self.ip = ip

    def send_bash_command(self, command:str):
        output = subprocess.run(args=["sshpass",
                                      "-p",
                                      self.password,
                                      "ssh",
                                      f"{self.user}@{self.ip}",
                                      command],
                                capture_output=True,
                                text=True,
                                check=True
                                )

        return output.stdout

    def send_bash_command_para(self, command: str) -> str:
        import paramiko

        client = paramiko.SSHClient()
        # Automatically accept the remote host key on first connection.
        # In production, replace with a known_hosts-based policy.
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(
                hostname=self.ip,
                username=self.user,
                password=self.password,
            )
            _, stdout, _ = client.exec_command(command)
            return stdout.read().decode()
        finally:
            # Always close the transport even if exec_command raises.
            client.close()

    def make_a_list_from_str_contains_new_line(self, sss: str):

        items = []
        nsss = ""

        for item in sss:
            if item != "\n":
                nsss += item
            else:
                items.append(nsss)
                nsss = ""

        if nsss:
            items.append(nsss)

        return items

# sshpass -p changeme1@ ssh vboxuser1@192.168.0.152