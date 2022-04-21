"""
tests
"""
import sys

import pytest
from app import methods


# @pytest.mark.skip(reason="do not run yet")
def test_add():
    """Test adding"""

    assert methods.add(2, 5) == 7
    assert methods.add(0, 0) == 0
    assert methods.add(-1, -1) == -2
    assert methods.add(-1, 0) == -1
    print('add numbers tested')

@pytest.mark.parametrize('num1, num2, result', [
(4, 5, 9), ('Hello ', 'World', 'Hello World')
])
def test_add_parametized(num1, num2, result):
    """Test adding parameters"""
    assert methods.add(num1, num2) == result


@pytest.mark.skipif(sys.version_info < (3, 3), reason='wont work')
def test_add_strings():
    """
    test add strings
    """
    result = methods.add('Hello ', 'World')
    assert result == 'Hello World'
    assert isinstance(result, str)

def test_multiply():
    """Test mult"""

    assert methods.multiply(0, 2) == 0

def test_multiply_strings():
    """Test mult str"""
    assert methods.multiply('Hello ', 3) == 'Hello Hello Hello '
    result = methods.multiply('Hello')
    assert 'Hello' in result
