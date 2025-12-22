def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must >= 0")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("n must >= 0")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)
