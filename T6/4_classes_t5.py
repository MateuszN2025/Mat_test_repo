
class Book:
    counter = 0
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        Book.counter += 1

    def __str__(self):
        return f"{self.title} {self.author} {self.pages}"

    def __eq__(self, other):
        return self.title == other.title

    def __lt__(self, other):
        return self.pages < other.pages

    def __le__(self, other):
        return self.pages <= other.pages

    def __add__(self, other):
        return self.pages + other.pages

    def __contains__(self, item):
        return item in self.title


b1 = Book("Lord","Tolkien",300)
b2 = Book("Lord","Tolkien",300)
b3 = Book("Narnia","Lewis",200)
print(b1)
print(b2)
print(b3)
print(f"|{Book.counter}|")
print(b1 == b2)
print(b1 < b2)
print(b1 <= b2)
print(b1 + b2)
print("-------")
print("Lord" in b1)
print("Man" in b1)

print("-------")

class Anyclass:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, int):
            return self.value + other
        else:
            return self.value + other.value

    def __radd__(self, other):
        return self.__add__(other)


a1 = Anyclass(5)
a2 = Anyclass(10)

print(a1 + a2)
print(a1 + 100)
print(21 + a2)

















