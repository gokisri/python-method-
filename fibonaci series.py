from functools import reduce

# Lambda function to generate Fibonacci sequence starting from 1
fibonacci_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [1, 1])

# Generate and print the first 50 Fibonacci numbers
fib_50 = fibonacci_series(50)
print(fib_50)

