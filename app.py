import math

def calculate_factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is not defined for negative numbers or non-integers.")
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
