def func(*args):
    return sum(args)

print(func(1,2,3,4,4))
print(func(2213,232))

def func2(**kwargs):
    for key, value in kwargs.items():
        print(f"key: {key}, value: {value}")

func2(a="aa", b="bb")


def func3(*args, **kwargs):
    i = 0
    for a in args:
        if a is list:
            for b in a:
                print(a**2)
        else:
            print(f"iteration number {i} : {a}")
            print(a)
        i+=1

    for b in kwargs:
        print(f"key is: {b}")

func3(12,32,32,42, key1=1, key2=2)
func3(12,[1,11,111],32,42, a="zz", b="zzzz")
