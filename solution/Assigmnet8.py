def alphabet_pattern_4(n):
    i = 1
    while i <= n:
        # Print leading spaces
        print(" " * (n - i), end="")
        
        # Print the increasing sequence
        for j in range(1, i + 1):
            print(chr(64 + j), end=" ")

        # Print the decreasing sequence
        for j in range(i - 1, 0, -1):
            print(chr(64 + j), end=" ")

        # Move to the next line
        print()
        i += 1

# Test
n = 3
alphabet_pattern_4(n)
