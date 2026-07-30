# t1 = [6,3,5,11] -> [3, 5, 6, 11]
# t2 = [3,6,8,1] -> [1,2,6,8]

t1 = [6,3,5,11]
t2 = [3,6,8,1] 

def table_merger(list1: list, list2: list) -> list:
    for_length = max([len(list1), len(list2)])
    l1_sorted = sorted(list1)
    l2_sorted = sorted(list2)
    result_table = []
    for i in range(for_length):
        for j in range(for_length):
            if l1_sorted[i] > l2_sorted[j]:
                result_table.append(l1_sorted[i])
            else:
                result_table.append(l2_sorted[j])
                
    return result_table

print(table_merger(t1, t2))