from function_for_bash import Basher

b = Basher(user="vboxuser1",
           password="changeme1@",
           ip="192.168.0.152")

out = b.send_bash_command("ls")
print(b.make_a_list_from_str_contains_new_line(out))
