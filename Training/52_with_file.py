with open('file1.txt','r') as f1:
    content1 = f1.readline()
    content2 = f1.readlines()

print(content1)
print(content2)