# input:  [2,7,13,17]
# target: [0,1]

l1 = [2,7,13,17]
#      0|1|2|3 

def return_target_indexes(list1: list, target1: int) -> list:
    i, j = 0, 0
    ll1 = len(list1)
    if (ll1) >= 2:
        print("Good list!")
        for i in range(ll1):
            for j in range(i+1, ll1):
                if list1[i] + list1[j] == target1:
                    return [i, j]
                    break
        return "target not achieved"                    
    else:
        print(f"List is too short, lenght: {ll1}")
    pass
print("-----------------ℹ️-------------------------")
print(return_target_indexes(list1=l1, target1=9))

print("-----------------ℹ️------------------------")

ll = len(l1)
start = 1
stop = 2
print(f"len(l1): {len(l1)}")

for i in range(start, stop):
    print(i)
    
print(range(start, stop))

print("------------------------------------------")
# range(2,2) -> no iterations: start == stop means we're already there
start2 = 2
stop2 = 2
print(f"range({start2}, {stop2}) -> {list(range(start2, stop2))}")
for i in range(start2, stop2):
    print(i)
print("loop done (0 iterations)")