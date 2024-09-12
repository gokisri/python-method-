from functools import reduce

# Lambda function to generate Fibonacci sequence
fibonacci_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

# Generate first 50 Fibonacci numbers
fib_50 = fibonacci_series(50)

# Display the result
fib_50
fibonacci_series_from_1 = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [1, 1])

# Generate first 50 Fibonacci numbers starting from 1
fib_50_from_1 = fibonacci_series_from_1(50)

# Display the result
fib_50_from_1
