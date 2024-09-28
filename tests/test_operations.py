'''My Calculator Test'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition method works'''
    assert add(5, 3) == 8

def test_subtraction():
    '''Test that subtraction method works'''
    assert subtract(9, 4) == 5

def test_multiplication():
    '''Test that multiplication method works'''
    assert multiply(6, 7) == 42

def test_division():
    '''Test that division method works'''
    assert divide(20, 5) == 4
