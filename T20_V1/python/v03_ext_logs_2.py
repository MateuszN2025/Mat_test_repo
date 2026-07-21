#TASK: extract just the component name 
# (the part in [...]) from each error line.

def mesg_counter(count: int, line: str) -> int:
    start_index = line.find("[")
    end_index = line.find("]")
    # Guard: skip lines that don't have a [...] component (e.g. blank lines, headers)
    if start_index == -1 or end_index == -1:
        return count
    print(line[start_index+1:end_index])
    count += 1
    return count

# count_err, count_info, count_warn = 0, 0, 0
count_mesg = 0
count_mesg_2 = 0
type_of_log = input("What type of logs you want? (ERROR|INFO|WARNING|ALL): ")
with open(file="v03_logs.txt", mode="r") as f:
    # lines = f.read() # call that was consuming the file before f.readlines(), 
    # which would have made the loop iterate over nothing.
    for line in f.readlines():
        if type_of_log == "ALL" or type_of_log in line:
            count_mesg = mesg_counter(count_mesg, line)
            print(f"count_mesg {count_mesg}")        
            print(f"mesg_counter(count_mesg_2, line) {mesg_counter(count_mesg_2, line)}")   
            # That = on the left is the key. The function returns 
            # the new value and the caller stores it back. 
            # So across loop iterations it accumulates: 0 → 1 → 2 → 3...
            # If you wrote this instead — outer count_mesg would NEVER change:
            #   mesg_counter(count_mesg, line)  # return value thrown away
            
            # Senior insight: This is why mutable objects (lists, dicts) 
            # behave differently — mutations inside a function do affect 
            # the caller's object, because both names point to the same 
            # object in memory. But integers? A new object is always created on +=.
            
            
print(f"{type_of_log}, amount: {count_mesg}")


# print(lines)
########################################################################
# because
# (.venv) root@LPT00356:/home/mniedziolka/PP/Mat_test_repo/
# 
# Cwd: /home/mniedziolka/PP/Mat_test_repo   ← you ran it from here
# Script: T20_V/python/v03_ext_logs_2.py