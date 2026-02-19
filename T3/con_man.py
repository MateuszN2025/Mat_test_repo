from contextlib import contextmanager

@contextmanager
def con_man():
    print("before")
    yield "1234"
    print("after")



with con_man() as con:
    print(con)
    print("Hello")

print("------------------------")
# kod przed yield to setup, po yield to cleanup.
@contextmanager
def con_man():
    print("before")
    yield "RESOURCE"
    print("after")

with con_man() as con:
    print("inside:", con)

"""
@contextmanager
def temp_env():
    os.environ["ENV"] = "test"
    yield
    os.environ.pop("ENV")
"""
