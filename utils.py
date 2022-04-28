import random


def get_input(n):
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            matrix[j][i] = matrix[i][j] = 0 if i == j else random.randint(0, 1)
    # for i in matrix:
    #     print(i)
    return matrix


get_input(10)


def get_polarized_network(n):
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i):
            k = random.randint(0, 3)
            if k == 1:
                matrix[i][j] = 'F'
            elif k == 2:
                matrix[i][j] = 'E'
            else:
                matrix[i][j] = 'U'
            matrix[j][i] = matrix[i][j]
    for i in range(n):
        matrix[i][i] = 'F'
    return matrix
