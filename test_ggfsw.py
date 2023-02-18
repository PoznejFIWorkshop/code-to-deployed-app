from logic import factorial

def test_factorial_positive_number():
    assert factorial(5) == 120


def test_factorial_zero():
    assert factorial(0) == 1