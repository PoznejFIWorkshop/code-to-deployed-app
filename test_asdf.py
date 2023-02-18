from logic import factorial

def test_factorial_positive():
    assert factorial(4) == 24

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1