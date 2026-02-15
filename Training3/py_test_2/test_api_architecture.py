import pytest

@pytest.mark.v1
def test1():
    print("test1")

@pytest.mark.v2
def test2():
    print("test2")

@pytest.mark.v3
def test3():
    print("test3")

@pytest.mark.version("v4")
def test4():
    print("test4")

@pytest.fixture()
def product_version():
    return "v543"

def test5(product_version):
    if product_version == "v543":
        assert 3 == 3
        print("test5_v543")
    else:
        assert 3 == 4
        print("test5_other")

@pytest.mark.parametrize("version", ["v1", "v2"])
def test6(version):
    print(f"version:{version}")

