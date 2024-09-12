data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x: x > 4, data)
print(list(result))



output:
[10, 501, 22, 37, 100, 999, 87, 351]

The filter function applies the lambda function lambda x: x > 4 to each element of the data list. Since all the elements in the list are greater than 4, none of them are filtered out.
