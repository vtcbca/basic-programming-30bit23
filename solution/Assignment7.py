def print_row(i, n):
    if i > n:
        return
    # Leading spaces
    print(" " * (n - i), end="")
    # Print numbers
    print(*range(1, 2 * i))
    # Recurse for the next row
    print_row(i + 1, n)

def triangle_pattern_4(n):
    print_row(1, n)

# Test
n = 3
triangle_pattern_4(n)
