import json


def write_json(file_path="files/example.json", data=None, indent=4):
    """
    Write data to a JSON file.

    Args:
        file_path (str): Path to the JSON file
        data (dict): Data to write (defaults to a sample dictionary if None)
        indent (int): Indentation level for pretty printing

    Returns:
        dict: The data that was written to the file
    """
    if data is None:
        data = {"name": "John", "age": 100}

    # Create directory if it doesn't exist
    import os
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Use 'with' statement for automatic file closure
    with open(file_path, "w") as file:
        json.dump(data, file, indent=indent)

    return data


# read
def read_file(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            # print(data)
    except FileNotFoundError:
        data = {}
    return data


def add_properties(file_path, new_properties):
    data = read_file(file_path)
    for key, val in new_properties.items():
        data[key] = val

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(data)
    return data


new_prop = {
    "version": "2.0",
    "debug_mode": True,
    "max_connections": 100
}

write_json()
add_properties('files/example.json', new_prop)
