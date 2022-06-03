import random
import queue
import graphMaker as gm
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['STZhongsong']    # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题


# 生成一组全序的偏好关系，tag[i] = rank，表示这个人对第i个物品放在了第rank位
# 这样定义的做法是为了降低时间复杂度
from matplotlib import pyplot as plt


def make_preference(n):
    tag = [False] * n
    res = []
    print(tag)
    while len(res) < n:
        k = random.randint(0, n - 1)
        if not tag[k]:
            tag[k] = True
            res.append(k + 1)
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 检查是否是DAG，只需要判断是否存在拓扑序
def check_DAG(matrix):
    n = len(matrix)
    que = queue.Queue(maxsize=n)
    deg = [0] * n
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                deg[j] += 1
    res = []
    for i in range(n):
        if deg[i] == 0:
            res.append(i)
            que.put(i)
    print(deg)
    while not que.empty():
        t = que.get()
        for to in matrix[t]:
            if matrix[t][to] == 1:
                deg[to] -= 1
                if deg[to] == 0:
                    que.put(to)
    print(res)
    return res


# 获取a与b的群体偏好关系
def get_prefer(preference, a, b):
    count = 0
    for prefer in preference:
        if prefer[a - 1] > prefer[b - 1]:
            count += 1
    if count > len(preference) / 2:
        return True
    return False


# 检查是否违背孔多塞悖论
def check_condorcet(preference, n, m):
    # 生成C(n, 2)组关系，判断是否是DAG
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i):
            if get_prefer(preference, i + 1, j + 1):
                matrix[i][j] = 1
            else:
                matrix[j][i] = 1
    # 根据邻接矩阵画图
    edges = []
    print(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                edges.append((i, j))
    gm.paint_(n, edges, "群体偏好图")
    return check_DAG(matrix)


# 判断一个偏好关系是否是单峰的
def check_peak(prefer):
    tag = False
    n = len(prefer)
    for i in range(n - 1):
        if not tag:
            if prefer[i] < prefer[i + 1]:
                tag = True
        else:
            if prefer[i] > prefer[i + 1]:
                return False
    return True


# 按照中位项定理排序
def get_median_term_order(preference):
    n = len(preference[0])
    for i in preference:
        print(i)
    after_prefer = []
    for prefer in preference:
        if check_peak(prefer):
            after_prefer.append(prefer)
    print()
    print()
    for i in after_prefer:
        print(i)
    # 将偏好关系从排名模式，转换到实际存储数据的模式
    m = len(after_prefer)
    real_preference = [[0] * n for i in range(m)]
    # 绘制剔除后的排名图，发现所有的都是单峰的
    x = [(i + 1) for i in range(n)]
    for prefer in after_prefer:
        paint(x, prefer)
    plt.show()
    # 剔除出不满足单峰性质的偏好关系后，使用中位项定理求解序列
    for i in range(m):
        for j in range(n):
            real_preference[i][after_prefer[i][j] - 1] = j + 1
    for i in real_preference:
        print(i)
    # 中位项定理
    order = []
    for k in range(n):
        temp = []
        for j in range(m):
            temp.append(real_preference[j][0])
        temp.sort()
        print("temp")
        print(temp)
        order.append(temp[int(m / 2)])
        for j in range(m):
            real_preference[j].remove(temp[int(m / 2)])
        print(order)


def paint(x, y):
    plt.xlabel('节点编号')
    plt.ylabel('喜爱排名')
    # plt.scatter(x, y, s=2, marker='*')  # s表示面积，marker表示图形
    plt.plot(x, y)
    # plt.show()


def main():
    n = 10  # 对n个物体进行表决
    m = 6  # 有m个人参与表决
    # 生成m个人对n个物品的偏好情况
    preference = [[10, 9, 1, 2, 3, 4, 5, 6, 7, 8],
                  [6, 5, 4, 3, 2, 1, 7, 8, 9, 10],
                  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                  [10, 7, 6, 3, 2, 1, 4, 5, 8, 9],
                  [2, 3, 1, 4, 6, 7, 9, 10, 5, 8],
                  [9, 5, 4, 2, 1, 3, 6, 7, 8, 10]]
    # 随机生成数据，发现很难得到一组满足要求的数据，于是变固定了数据
    x = [(i + 1) for i in range(n)]
    for prefer in preference:
        paint(x, prefer)
    plt.show()
    # for i in range(m):
        # preference.append(make_preference(n))
    # 确定是否存在孔多塞悖论
    order = check_condorcet(preference, n, m)
    if len(order) == n:
        # 如果没有违背孔多塞悖论，则直接输出排序结果
        print(order)
    else:
        # 如果有违背孔多塞悖论，则判断出是那些不满足单峰性质
        get_median_term_order(preference)


if __name__ == "__main__":
    main()
