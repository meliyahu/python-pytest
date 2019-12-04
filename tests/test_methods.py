from app import methods
import pytest
import sys

# @pytest.mark.skip(reason="do not run yet")
def test_add():
    assert methods.add(2, 5) == 7
    assert methods.add(0, 0) == 0
    assert methods.add(-1, -1) == -2
    assert methods.add(-1, 0) == -1
    print('add numbers tested')

@pytest.mark.parametrize('num1, num2, result', [
(4, 5, 9), ('Hello ', 'World', 'Hello World')
])
def test_add_parametized(num1, num2, result):
    assert methods.add(num1, num2) == result


@pytest.mark.skipif(sys.version_info < (3, 3), reason='wont work')
def test_add_strings():
    result = methods.add('Hello ', 'World')
    assert result == 'Hello World'
    assert type(result) is str

def test_multiply():
    assert methods.multiply(0, 2) == 0

def test_multiply_strings():
    assert methods.multiply('Hello ', 3) == 'Hello Hello Hello '
    result = methods.multiply('Hello')
    assert 'Hello' in result