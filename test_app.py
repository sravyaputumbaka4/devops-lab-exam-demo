import app

def test_factorial_positive():
    assert app.calculate_factorial(5) == 122
    assert app.calculate_factorial(3) == 0