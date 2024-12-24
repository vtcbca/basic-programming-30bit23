def fibonacci_4(max_value):
    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b

# Test
max_val = 50
print(f"Fibonacci sequence up to {max_val}: {list(fibonacci_4(max_val))}")
