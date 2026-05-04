import w_r
from collections import Counter, defaultdict, deque

@w_r
def main():
    # ##################################
    list1 = [1,2,3,4,5,4,4,3,2,2,3,2]
    c = Counter(list1)
    print(c) # Counter({2: 4, 3: 3, 4: 3, 1: 1, 5: 1})
    print(dict(c))
    print("------------------------------------------")
    list2 = ["cat", "dog", "donkey", "caterpillar"]
    # d = defaultdict(list)
    # for item in list2:
    #    first_letter = item[0]
    #    d[first_letter].append(item)
    # print(dict(d))  
    d = {}
    for item in list2:
        d.setdefault(item[0], []).append(item)
    print(d)  # {'c': ['cat','caterpillar'], 'd': ['dog','donkey']}
    d["c"].append("a")
    print(d)
    print("------------------------------------------")
    q = deque()
    print(q)
    print((q.append("a")))
    print(list(q))
    q.appendleft("START")
    print(list(q))
    q.appendleft("LEFT")
    list3 = list(q)
    print(list3)
    # ##################################
main()