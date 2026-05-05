from collections import Counter, defaultdict, deque
import w_r


@w_r
def main():
    list1 = [_ for _ in range(10)]
    # print(list1)
    list1.append(9)
    count = dict(Counter(list1))
    print(count)
    print("------------------------------------------")
    # defaultdict: automatically creates a default value if key does not exist.
    list2 = ["mamma", "tatta", "tatoo", "mimi"]
    dict1 = defaultdict(list)
    for item in list2:
        dict1[item[0]].append(item)
    print(f"{dict(dict1)}")
    print("------------------------------------------")
    q = deque()
    q.append("A")
    q.appendleft("B")
    q.appendleft("C")
    print(list(q))
    q.pop()
    print(list(q))
    q.popleft()
    print(list(q))
main()