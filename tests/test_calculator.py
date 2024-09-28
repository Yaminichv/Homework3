''' My Calculator Test '''
import pytest
from calculator import Calculator

def test_add():
    '''Tests the addition method'''
    assert Calculator.add(7, 8) == 15

def test_subtract():
    '''Tests the subtraction method'''
    assert Calculator.subtract(10, 4) == 6

def test_multiply():
    '''Tests the multiplication method'''
    assert Calculator.multiply(6, 7) == 42

def test_divide():
    '''Tests the division method'''
    assert Calculator.divide(20, 4) == 5

def test_dividebyzero():
    '''Tests if division by zero throws an error'''
    with pytest.raises(ValueError):
        Calculator.divide(15, 0)
