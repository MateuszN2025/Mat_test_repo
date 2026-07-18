print("------------------------------------------")
dict1 = {"aa": 543, "cc": 89098, "zzz": 232}
dict2 = dict(g = 5, ccc = 55, k = 909)
print(dict1)
print(dict2)
input_to_list1 = dict1.keys()
print(dict1.keys())
print(list(input_to_list1))
print(type(dict1.keys()))
print(list(dict1.values()))
dict1.update(dict2)
print(dict1)
print(list(dict1.values()))
print(tuple(dict1.items()))
print(list(dict1.items()))
print(dict1.pop('g'))
print(dict1)
print(dict1.get("john"))
print(dict1)
print(dict1["k"])

data = ["PASS", "FAIL", "PASS", "SKIPPED"]
def task_dict_count_statuses(statuses: list) -> dict:
    """
	Count how many times each status appears.
	Input: ["PASS", "FAIL", "PASS"]
	Output: {"PASS": 2, "FAIL": 1}
	"""
    # pass_c = statuses.count("PASS")
    # fail_c = statuses.count("FAIL")    
    # return {"PASS": pass_c, "FAIL": fail_c}
    
    # counter = {}
    # for status in statuses:
    #  counter[status] = counter.get(status, 0) + 1
    # return counter

    counter = {}
    for status in statuses:
        if status in counter:
            counter[status] += 1
        else:
            counter[status] = 1
    return counter

print(task_dict_count_statuses(data))