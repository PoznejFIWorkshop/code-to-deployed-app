from logic import factorial

def test_fucktorial():
    assert factorial(4) == 24

    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(7) == 5040

def test_faktorial():
    assert factorial(0) == 1

