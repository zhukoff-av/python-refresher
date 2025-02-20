def add_element(
        new: list[str] | str,
        src: list = []) -> list:
    if isinstance(new, list):
        src.extend(new)
    else:
        src.append(new)
    return src


if __name__ == "__main__":
    value1 = add_element("test")
    print(value1)
    value2 = add_element(["test2", "test3"])
    print(value2)
    value3 = add_element(["test4"], value2)
    print(value3)
