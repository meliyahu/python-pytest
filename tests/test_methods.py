from app import methods
def test_add():
    assert methods.add(2, 5) == 7
    assert methods.add(0, 0) == 0
    assert methods.add(-1, -1) == -2
    assert methods.add(-1, 0) == -1

def test_multiply():
    assert methods.multiply(0, 2) == 0