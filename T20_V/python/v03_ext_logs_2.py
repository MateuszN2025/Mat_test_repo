#TASK: extract just the component name 
# (the part in [...]) from each error line.


with open(file="v03_logs.txt", mode="r") as f:
    lines = f.read()
    for line in f.readlines():
        start_index = line.find("[")
        end_index = line.find("]")
        print(line[start_index:end_index+1])


# print(lines)

