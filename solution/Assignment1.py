def factorial_4(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Test
n = 5
print(f"Factorial of {n} is: {factorial_4(n)}")
