from logic import factorial

def test_fact_0():
    assert factorial(0) == 1

def test_fact_3():
    assert factorial(3) == 6

def test_fact_negative():
    try:
        factorial(-10)
    except AssertionError:
        return
    assert False, "Factorial shouldn't work for negative numbers"

def test_fact_concecutive_numbers():
    assert 100*factorial(99) == factorial(100)

if __name__ == "__main__":
    print("Try calling this file with: python3 -m pytest .")
