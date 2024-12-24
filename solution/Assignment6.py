def pattern_4(n):
    for i in range(1, n + 1):
        print(" ".join(["*"] * i))

# Test
n = 4
pattern_4(n)
