import random


# 生成n * n 邻接矩阵
def get_input(n):
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            matrix[j][i] = matrix[i][j] = 0 if i == j else random.randint(0, 1)
    # for i in matrix:
    #     print(i)
    return matrix


# 生成极化网络
def get_polarized_network(n):
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i):
            k = random.randint(0, 7)
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


# 生成异值门槛网络
def get_threshold(n):
    threshold = [0] * n
    for i in range(n):
        threshold[i] = random.randint(0, 10) / 10
    return threshold


# 生成初始节点
def get_init(n, m):
    res = set()
    while len(res) < m:
        k = random.randint(0, n - 1)
        res.update({k})
    return res
