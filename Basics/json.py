import json

person = {
    "name": "<NAME>",
    "age": 22,
    "height": 177,
    "weight": 80,
}

json_string = json.dumps(person)

person_str = '{"name": "<NAME>", "age": 22, "height": 177, "weight": 80}'
person_json = json.loads(person_str)

print(person_json)
