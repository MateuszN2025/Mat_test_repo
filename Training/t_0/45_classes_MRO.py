class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()

d = D()
print(D.mro())
"""
super() nie oznacza „idź do rodzica”, tylko „idź do następnej klasy w MRO”.
Dzięki temu Python unika powtarzania metod w wielokrotnym dziedziczeniu.
D.mro() pozwala Ci sprawdzić kolejność, w jakiej metody będą wyszukiwane.
D → B → C → A → object

Intuicja
B jest pierwszy, więc idziemy do B.
Ale zanim wrócimy do A, musimy jeszcze przejść przez drugiego rodzica C (bo D tak zostało zadeklarowane).
Dopiero gdy obaj bezpośredni rodzice (B i C) są „obsłużeni”, przechodzimy do wspólnego przodka (A).
"""