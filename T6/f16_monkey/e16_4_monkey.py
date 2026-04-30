import wrapping
from functools import wraps

COUNTER = 0

def printer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global COUNTER
        COUNTER += 1
        print(f"{COUNTER:>2} calling: {func.__name__:<8}: c1.sound() ", end="")
        return func(*args, **kwargs)

    return wrapper


class Car:
    @printer
    def sound(self):
        return "BRUMMMM"
    
    def sound2():
        return "WZIUUUM"

@printer
def monkey():
    return "MONKEY"

@wrapping
def main():
    # ##################################
    
    c1 = Car()
    print(f"{c1.sound()}")
       
    c1.sound = monkey
    print(f"{c1.sound()}") 
    
    """IMPORTANT"""
    del c1.sound # <===
    print(f"{c1.sound()}") 
    
    c1.sound = monkey
    print(f"{c1.sound()}")
    
    c1.sound = Car.sound.__get__(c1, Car) # <===
    print(f"{c1.sound()}")
    
    print("------------------------------------------")
    """IMPORTANT"""
    original_sound2 = Car.sound2

    print(f"{Car.sound2()}")
    Car.sound2 = monkey
    print(f"{Car.sound2()}")
    Car.sound2 = original_sound2
    print(f"{Car.sound2()}")
    
    
    # ##################################
main()