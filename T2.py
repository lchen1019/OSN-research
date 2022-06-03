import random
import utils
import MakeData_
import MakeData
import matplotlib.pyplot as plt
import numpy as np

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['STZhongsong']    # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题


def paint(x, y):
    plt.xlabel('节点数')
    plt.ylabel('符合比例')
    plt.scatter(x, y, s=2, marker='*')  # s表示面积，marker表示图形
    plt.show()


def get_everyone_friends(matrix, n):
    res = [0] * n
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                res[i] += 1
    return res


def solve(matrix, n):
    friends = get_everyone_friends(matrix, n)
    conform = 0
    for i in range(n):
        sum_friends = 0
        for j in range(n):
            if matrix[i][j] == 1:
                # 计算所有朋友的朋友数量之和
                sum_friends += friends[j]
        if sum_friends > friends[i] * friends[i]:
            conform += 1
    print("符合友谊悖论的比例为：{:.5f}".format(conform / n))
    return conform / n


# 随机生成图的验证
def random_graph():
    cnt = 0
    x = []
    y = []
    while cnt < 1000:
        n = random.randint(10, 500)
        x.append(n)
        matrix = utils.get_input(n)
        y.append(solve(matrix, n))
        print(cnt)
        cnt += 1
    paint(x, y)


# 实际社会网络的验证
def real_graph():
    matrix = MakeData.get_matrix()
    solve(matrix, len(matrix))


def main():
    random_graph()
    real_graph()


if __name__ == "__main__":
    main()
