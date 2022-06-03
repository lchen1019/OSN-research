import random
import utils


# 计算聚集系数，指的是节点A的任意邻居也是朋友的概率
def get_clustering_coefficient(matrix, n, a):
    neighbor = []
    for i in range(n):
        if matrix[a][i] == 1:
            neighbor.append(i)
    tot_friends = 0
    if len(neighbor) == 1 or len(neighbor) == 0:
        return 0
    for i in range(len(neighbor)):
        for j in range(len(neighbor)):
            if matrix[i][j] == 1:
                tot_friends += 1
    tot_combination = len(neighbor) * (len(neighbor) - 1) / 2
    return tot_friends / tot_combination


# 计算邻里重叠度
def get_neighbor_overlap(matrix, n, a, b):
    # 统计a, b有多少朋友
    total_friend = []
    same_friend = []
    for i in range(n):
        if matrix[a][i] == 1 or matrix[b][i] == 1:
            total_friend.append(i)
        if matrix[a][i] == 1 and matrix[b][i] == 1:
            same_friend.append(i)
    return len(same_friend) / len(total_friend)


def main():
    # 随机生成邻接矩阵
    n = random.randint(10, 20)
    matrix = utils.get_input(n)
    print("输入数据: ")
    print("一共有{}个节点".format(n))
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()
    # 计算任意点的聚集系数
    print("聚集系数")
    clustering_coefficient = [0] * n
    for i in range(n):
        clustering_coefficient[i] = get_clustering_coefficient(matrix, n, i)
    for i in range(n):
        print("{:.3f}".format(clustering_coefficient[i]), end=' ')
    print()

    # 计算任意点对的邻里重叠度
    print("邻里重叠度：")
    neighbor_overlap = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            neighbor_overlap[j][i] = neighbor_overlap[i][j] = 1 if i == j else get_neighbor_overlap(matrix, n, i, j)
    for i in range(n):
        for j in range(n):
            print("{:.3f} ".format(neighbor_overlap[i][j]), end=' ')
        print()


if __name__ == "__main__":
    main()
