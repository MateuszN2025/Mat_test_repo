with open('file1.txt','r') as f1:
    content1 = f1.readline()
    content2 = f1.readlines()

print(content1)
print(content2)

file_table = []
i=0

with open('file1.txt', 'w') as f2:
    for number in range(101):
        if number == 0:
            f2.write(" " + str(number))
            continue
        if number > 0 and number <= 10:
            f2.write("  " + str(number))
        else:
            f2.write(" " + str(number))
        if number % 10 == 0:
            f2.write("\n")

with open('file1.txt', 'w') as f2:
    for number in range(101):
        # if number == 0:
        #     f2.write(" " + str(number))
        #     continue
        if number > 0 and number <= 10:
            f2.write("  " + str(number))
        else:
            f2.write(" " + str(number))
        if number % 10 == 0:
            f2.write("\n")
