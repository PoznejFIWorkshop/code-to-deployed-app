from logic import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_positive_number():
    assert factorial(4) == 24

def test_factorial_not_minus():
    assert factorial(4) >= 1