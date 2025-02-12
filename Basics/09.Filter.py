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


def filter_by_age(person: dict) -> bool:
    return person["age"] >= 18


print(list(filter(filter_by_age, people)))
