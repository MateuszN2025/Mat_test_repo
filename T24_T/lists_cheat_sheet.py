logs = ["PASS", "FAIL", "PASS"]
logs.append("ERROR")
print(logs)
logs.remove("FAIL")
print(logs)
logs.insert(0, "MONKEY")
print(logs)
logs2 = ["SKIPPED", "SKIPPED", "SKIPPED"]
logs.extend(logs2)
print(logs)
print(logs.pop())
print(logs)
print(logs.pop(1))
print(logs)
print(logs.count("PASS"))
print(logs.count("SKIPPED"))
print(logs.index("SKIPPED"))
# logs.sort()
print(logs)
new_list = sorted(logs)
print(new_list)
print("------------------------------------------")
rev_list = list(reversed(logs))
print(rev_list)
print("------------------------------------------")
print(rev_list[1:]) # 'SKIPPED', 'ERROR', 'PASS', 'MONKEY']
print(rev_list[1:4]) # SKIPPED', 'ERROR', 'PASS', 
print(rev_list[-5:-3]) # ['SKIPPED', 'SKIPPED',
co_list = rev_list.copy()
print(co_list)
print(id(rev_list))
print(id(co_list))
co_list2 = co_list
print(id(co_list2))
print("------------------------------------------")
"""
Return only failed test ids.
Input: [("T1", "PASS"), ("T2", "FAIL")]
Output: ["T2"]
"""
data = [("T1", "PASS"), ("T2", "FAIL"), ("T3", "FAIL")]
def func(items: list) -> list:
    # result = []
    # for item in items:
    #     if item[1] == "FAIL":
    #         result.append(item)
            
    # for i in range(len(result)):
    #     result[i] = result[i][0]
    
    # result = []
    # for item in items:
    #     test_id, status = item
    #     if status == "FAIL":
    #         result.append(test_id)                 
    # return result
    
    return [test_id for test_id, status in items if status == "FAIL"]

print(func(data))