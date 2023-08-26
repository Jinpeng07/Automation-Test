import pytest

data = [
    (10, 20, 30),
    (40, 50, 90)
]

ids = ["a:{}+b:{}=expect:{}".format(a, b, expect) for a, b, expect in data]


def add(a, b):
    return a + b


@pytest.mark.parametrize("a,b,e", data, ids=ids)
def test_maker(a, b, e):
    print("\ntest_maker")
    print("a=%d,b=%d,e=%d" % (a, b, e))
    assert add(a, b) == e


if __name__ == '__main__':
    pytest.main(["test26_2.py"], "-s")
