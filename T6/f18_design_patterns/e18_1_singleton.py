import w_r
from threading import Lock


# class Sing:
#     _instance = None
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance    

# @w_r
# def main():
#     s1 = Sing()
#     s2 = Sing()
#     print(s1 is s2)

# main()


class Sing:
    _instance = None
    _lock = Lock() # Shared lock to protect singleton creation in multi-threaded code.
    # The lock is used to prevent two threads from 
    # creating the singleton instance at the same time.
    
    def __new__(cls):
        if cls._instance is None:
            # Lock only during first creation to keep the singleton thread-safe.
            with cls._lock:
                if cls._instance is None:
                    # __new__ creates the object only once and reuses it later.
                    cls._instance = super().__new__(cls)
                

        return cls._instance

    def __init__(self):
        # Skip repeated setup because __init__ runs on every Sing() call.
        if getattr(self, "_initialized", False):
            return

        self.value = "created once"
        self._initialized = True

@w_r
def main():
    s1 = Sing()
    s2 = Sing()

    print(s1 is s2)
    print(s1.value)
    print(s2.value)

main()