import csv

data = [
    ["name", "age", "city"],
    ["John", 33, "NY"],
    ["Areo", 13, "London"],
    ["Brno", 83, "Prague"]
]

file = open("files/data.csv", "w")
csv_writer = csv.writer(file)
csv_writer.writerows(data)
file.close()
