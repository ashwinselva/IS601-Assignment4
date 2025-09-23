# tests/test_calculator_basic.py
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5.0

def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6.0

def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 2.5) == 7.5

def test_divide():
    calc = Calculator()
    assert calc.divide(9, 4.5) == 2.0
