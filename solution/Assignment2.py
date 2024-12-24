def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes

def is_prime_4(n):
    if n <= 1:
        return False
    primes = sieve_of_eratosthenes(n)
    return primes[n]

# Test
test_numbers = [11, 14, 23, 35, 17]
for number in test_numbers:
    print(f"Is {number} prime? {is_prime_4(number)}")
