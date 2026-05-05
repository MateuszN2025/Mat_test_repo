import w_r

class MetaMeta(type):
    def __new__(mcls, name, bases, namespace):
        namespace["var_a"] = True       
        
        # bases contains the parent classes declared in the class header.
        print(f"name: {name} | bases:{bases}")
        
        if "Normal" not in name:
            raise NameError("Class name must contains word 'Normal'❗")
        else:
            return super().__new__(mcls, name, bases, namespace)
    
class NormalClass(metaclass=MetaMeta):
    pass

# class BoringClass(metaclass=MetaMeta):
#     pass

class BoringNormalClass(metaclass=MetaMeta):
    pass

class BoringNormalClass2(NormalClass):
    #                                                      |parent|
    # name: BoringNormalClass2 | bases:(<class '__main__.NormalClass'>,)
    pass

class BigString(str):
    def __new__(cls, word:str):
        return super().__new__(cls, word.upper()) # ❗cls must be forwarded openly
    
        # self is forwarded automatically
        # class A:
        #   def init(self, x):
        #   print("A init", x)
        # class B(A):
        # def init(self, x):
        #   super().init(x)        

# @w_r
def main():
    n1 = NormalClass()
    print(n1.var_a)
    b1 = BoringNormalClass()
    print(b1.var_a)
    w1 = BigString("ascd")
    print(w1)
    print("------------------------------------------")
    b2 = BoringNormalClass2()
    print(b2.var_a)

    # Immutable subclasses must be constructed by the matching base type __new__.
    # def __new__(cls, word:str):
    print(str.__new__(BigString, "abc"))
    print("------------------------------------------")
    print(type(w1), isinstance(w1, BigString))
    print("------------------------------------------")

    try:
        print(object.__new__(BigString))
    except TypeError as error:
        print(error)

    
main()    