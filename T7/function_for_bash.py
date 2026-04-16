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
