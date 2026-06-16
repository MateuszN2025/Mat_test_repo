import subprocess
subprocess.run(args="clear")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")

# [[1,2,3],[1,2,3]],[1,2,3]

# r = 4

# table1 = [x for x in range(1, r)]
# table2 = [x for x in range(1, r)]

# print(f"{table2}")

# for i in range(len(table1)):
#     table1[i] = list(table2)

# print(f"{table1}")
        
# r = 4
# table = [list(range(1, r)) for _ in range(1, r)]
# print(table)

r = 11

table2d = []
table = [x for x in range(1, r)]

# for i in range(len(table)):
#     table2d.append(list(table))
    
table2d = [list(table) for _ in range(len(table))]    


for ii in range(len(table2d)):
    print(f"{table2d[ii]}", end="\n")

print(table2d)
    
    
# print(table2d[8][8])

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303
