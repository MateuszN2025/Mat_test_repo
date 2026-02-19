class A:
    def metoda(self):
        print("A")

class B:
    def metoda(self):
        print("B")

class C(A, B):
    pass

c = C()
c.metoda()  # Wyświetli: A (MRO - Method Resolution Order)
print("===================================")

def funk(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

funk(1, 2, 3, 4, imie="Jan", wiek=30)

print("===================================")
class X: pass
class Y: pass
class Z(X, Y): pass

print(Z.mro())  # Pokazuje kolejność dziedziczenia