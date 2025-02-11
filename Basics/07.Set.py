# set: unique numbers
print('Set: unique numbers')
numbers = [1, 2, 3, 4, 4, 1, 0, 1, 2]
unique_numbers = list(set(numbers))
print(unique_numbers)

set_1 = {0, 1, 2, 3, 4}
set_2 = {2, 4, 5}

# union
print('UNION')
result = set_1.union(set_2)
print(result)

# intersection
print('INTERSECTION')
result = set_1.intersection(set_2)
print(result)

# difference
print('DIFFERENCE')
result = set_1.difference(set_2)
print(result)