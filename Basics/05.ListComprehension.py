import json

numbers = [0, 2, 4, 5, 12, 435, 23, 23, 1, 9]
print([x ** 2 for x in numbers])

# even or odd in one line
print(["even" if x % 2 == 0 else "odd" for x in numbers])

# list comp. in a dict
dict = {x: x ** 2 for x in range(10)}
print(dict)
