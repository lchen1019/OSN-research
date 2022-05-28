import utils
import matplotlib.pyplot as plt
import graphMaker as gm
import tableMaker as tm


# 计算每一个节点的朋友个数
def get_all_neighbors(matrix):
    n = len(matrix)
    friends = [0] * n
    for i in range(n):
        k = 0
        for j in range(n):
            if matrix[i][j] == 1:
                k = k + 1
        friends[i] = k
    return friends


# 计算初始时一个人的朋友中接收新事物朋友的数量
def get_friends_spread(matrix, spread, spread_friends):
    for t in spread:
        for k in range(len(matrix)):
            if matrix[t][k] == 1:
                spread_friends[k] += 1


# 绘制扩散曲线
def paint_curve(x, y):
    plt.xlabel('时间')  # x轴标签
    plt.ylabel('接受规模')  # y轴标签
    plt.plot(x, y)  # 绘制图像
    plt.show()  # 显示图像


def main():
    n = 200
    m = n * 0.01
    # 随机生成邻接矩阵和每一个节点门槛值
    matrix = utils.get_input(n)
    threshold = utils.get_threshold(n)
    # 初始化边集合，方便绘制图像
    edges = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                edges.append((i, j))
    # 随机生成初始化节点
    spread = utils.get_init(n, m)
    # 输出随机信息
    # for i in matrix:
        # print(i)
    # print(threshold)
    # print(spread)
    # 求出初始每一个节点的朋友数
    friends = get_all_neighbors(matrix)
    # print(friends)
    # 初始化每一个人的朋友中，接收新事物朋友的数量
    spread_friends = [0] * n
    get_friends_spread(matrix, spread, spread_friends)
    # print(spread_friends)
    # 初始化每一个节点是否已经接收新事物
    accept_tag = [False] * n
    for i in spread:
        accept_tag[i - 1] = True
    # 绘制初始门槛值
    tm.paint([threshold], [str(i + 1) for i in range(n)])
    # 绘制初始图像
    gm.paint(n, edges, "原始输入图", set())
    gm.paint(n, edges, "选择初始节点图", spread)
    # 每一轮扫描发生过更新节点的邻接节点情况
    # 不断循环更新，直到没有一轮中没有节点加入
    update_round = 1
    x = [1]
    y = [0.01]
    while True:
        update = False
        need_update = set()
        for i in range(n):
            # 如果大于门槛值，则这个节点可以被纳入
            if spread_friends[i] / friends[i] >= threshold[i] and not accept_tag[i - 1]:
                accept_tag[i - 1] = True
                need_update.update({i})
                update = True
        if not update:
            break
        # 更新传播到的朋友矩阵
        get_friends_spread(matrix, need_update, spread_friends)
        # print(need_update)
        # 绘制扩散图像
        spread.update(need_update)
        print(len(spread))
        gm.paint(n, edges, "第" + str(update_round) + "步扩散结果", spread)
        update_round += 1
        y.append(len(spread) / n)
        x.append(update_round)
    paint_curve(x, y)


if __name__ == "__main__":
    main()
