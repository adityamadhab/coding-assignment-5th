def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

prime_numbers = [n for n in range(1, 101) if is_prime(n)]

print(prime_numbers)
