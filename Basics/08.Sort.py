# sorted
from logging import getLevelName

persons = ['Aaac', 'Baac', 'Caac', 'Aaa']

print(sorted(persons))

# sort with function

people = [
    {"name": "Alain", "age": 33},
    {"name": "Ole", "age": 31},
    {"name": "Simon", "age": 53},
    {"name": "Alex", "age": 44},
    {"name": "Aaron", "age": 11},
    {"name": "Diana", "age": 33},
    {"name": "Omigo", "age": 31},
    {"name": "Cat", "age": 53},
    {"name": "DOG", "age": 44},
    {"name": "Stoun", "age": 11},
]


# sort by age
def sort_by_age(person: dict) -> int:
    return person["age"]


# sort by age and by name
def sort_by_age_name(people: dict) -> tuple[int, str]:
    return people["age"], people["name"]


sorted_people = sorted(people, key=sort_by_age_name)
sorted_list = sorted(people, key=sort_by_age)

print(sorted_people)
