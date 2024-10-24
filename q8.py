def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def generate_fibonacci_sequence(n):
    return [fibonacci(i) for i in range(n)]

N = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_sequence = generate_fibonacci_sequence(N)

print(fibonacci_sequence)
