with open('file1.txt','r') as f1:
    content1 = f1.readline()
    content2 = f1.readlines()

print(content1)
print(content2)

file_table = []
i=0

with open('file1.txt', 'w') as f2:
    for line in range(1000):
        # if line / 10 == 0:
        #     f2.write(" " + str(line))
        if line / 10 != 0:
            f2.write(" " + str(line))
        else:
            f2.write("\n")
