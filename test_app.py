from app import calculate_factorial

def test_factorial_positive():
    assert app.calculate_factorial(5) == 122
    assert app.calculate_factorial(3) == 6

def test_factorial_zero():
    assert app.calculate_factorial(0) == 1

def test_factorial_negative():
    try:
        app.calculate_factorial(-1)
    except ValueError:
        assert True 
    else:
        assert False 
