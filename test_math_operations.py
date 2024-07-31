from math_operations import add, subtract, multiply
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    

@pytest.mark.parametrize(
    "a, b, expected",
        [(2, 3, 5), (-1, 1, 0), (0, 0, 0), (1.5, 2.5, 4)]
        )
        
def test_add(a, b, expected):
    assert add(a, b) == expected
    
def test_subtract():
    assert subtract(5, 5) == 0

def test_multiply():
    assert multiply(2, 3) == 6
