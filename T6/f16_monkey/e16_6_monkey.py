import w_r

def monkey():
    print("🐒")
    
def hippo():
    print("🦛")
    

class Animal:
    def animal(self):
        print("ANIMAL")
        
    @staticmethod
    def animal2():
        print("ANIMAL2")

@w_r
def main():
    global hippo
    # ##################################
    monkey()
    hippo()   
    hippo = monkey
    hippo() 
    a1 = Animal()
    a1.animal()
    a1.animal = monkey
    a1.animal()
    del a1.animal
    a1.animal()
    original_func = Animal.animal2
    Animal.animal2()
    Animal.animal2 = monkey
    Animal.animal2()
    Animal.animal2 = original_func
    Animal.animal2()
    # ##################################

main()