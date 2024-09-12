# Define a list with mixed types
elements = [1, 'apple', 3, 'banana', 42, 'cherry']

# Lambda function to check if an element is an integer or a string
check_type = lambda x: 'Integer' if isinstance(x, int) else 'String' if isinstance(x, str) else 'Other'

# Apply the lambda function to each element in the list
result = list(map(check_type, elements))

# Print the result
for element, res in zip(elements, result):
    print(f"{element}: {res}")
