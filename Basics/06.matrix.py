matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose_matrix = []

for i in range(len(matrix)):
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
    transpose_matrix.append(transpose_row)

tr_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]

print(tr_matrix)

# print(transpose_matrix)
