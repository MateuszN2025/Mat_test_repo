import subprocess
import os
import json
from pathlib import Path
import csv

subprocess.run(args="clear")

# current_dir = os.path.dirname(os.path.abspath(__file__))
# print(current_dir)


current_dir = Path(__file__).resolve().parent
# print(current_dir)


print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")












list1 = [1, 2, 3, 4, 5]
list2 = ["Bob", "John"]
dict1 = {"a": 9080, "b": 3244}

"""
with open(f"{current_dir}/test.txt", "w") as f:
    # f.write(list1) # TypeError: write() argument must be str, not list
    for item in list1:
        f.write(str(item) + " ")
        
with open(f"{current_dir}/test_str.txt", "w") as f:
    # f.write(list1) # TypeError: write() argument must be str, not list
    for item in list2:
        f.write(item + "\n")
    # f.writelines(list2)
    # f.writelines(list2)
    # print(f"{help(open)}") 
    
with open(f"{current_dir}/test.json", "w") as f:
    f.write(json.dumps(dict1))
"""

# fjson = f"{current_dir}/test2.json"

    
# with open(fjson, "w") as f:
#     json.dump(fp=f, obj=dict1, indent=4)

# fcsv = f"{current_dir}/testcsv"
fcsv = f"{current_dir}/test.csv"

csv_list = [
    ["name", "age", "height"],
    ["John", 13, 160],
    ["Don", 23, 190]
]

with open(fcsv, "w") as f:
    # writer = csv.writer(f)
    # for data in csv_list:
    #     writer.writerow(data)
    for data in csv_list:
        csv.writer(f).writerow(data)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303
