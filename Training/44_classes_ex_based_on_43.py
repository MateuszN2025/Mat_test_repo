class Plain:
    def __init__(self, name: str, power: int):
        self.__name = name
        self._power = power

    def name_getter(self):
        return self.__name

    def __str__(self):
        return f"This is plain: {self.__name} with power: {self._power}"

    """
    p = Person("Jan", 30)
    to wywołanie:
    Person.__init__(p, "Jan", 30)
    """

class Boeing(Plain):
    def __init__(self, name, power, flight_hours):
        super().__init__(name, power) # zrobiłem błąd i dałem tutaj self a on jest
        # domyślnie przekazywany jak to jest opisane poniżej
        """
        class Student(Person):
            def __init__(self, name, age, student_id):
                super().__init__(name, age)  # tutaj!
                self.student_id = student_id
        
        to super().__init__(name, age) jest w praktyce równoważne:        
        Person.__init__(self, name, age)        
        czyli self już jest przekazany automatycznie przez mechanizm super()
        """
        self.flight_hours = flight_hours

    def __str__(self):
        return super().__str__() + f"and with flight_hours: {self.flight_hours}"

b = Boeing("a767", 10000, 4000)
print(b)
print(b._power)

print(b.name_getter())
# print(b._Plane__name) # AttributeError: 'Boeing' object has no attribute '_Plane__name'
# print(b._Boeing__name) # AttributeError: 'Boeing' object has no attribute '_Boeing__name'
p = Plain("f2343", 20000)
print(p._Plain__name)