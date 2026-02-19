class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_animal(self):
        print(f"name: {self.name}, age: {self.age}")

    def __str__(self):
        return f">>>{self.name}>>>{self.age}"

class Hasky(Animal):
    def __init__(self, name, age, level):
        super().__init__(name, age)
        self.level = level
    def __str__(self):
        return super().__str__() + f">>>{self.level}"

print("=================")
dog = Animal("dog1", 1)
print(dog.name)
print(dog.age)
dog.show_animal()
print(dog) # without __str__ it gives: <__main__.Animal object at 0x000001F6361E9400>
print("=================")
dog222 = Hasky("doggy", 2, 4000)
print(dog222)
print("=================")