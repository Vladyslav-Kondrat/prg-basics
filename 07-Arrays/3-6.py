matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

def change(matrix):
    for value in range(len(matrix)):
        matrix[value][value] = 1
    return matrix


modif_matrix = change(matrix)
for row in modif_matrix:
    print(row)