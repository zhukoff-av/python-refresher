# try except

def find_average(numbers: list) -> float:
    return sum(numbers) / len(numbers)


try:
    find_average(numbers=[])
except ZeroDivisionError as err:
    print(err)



