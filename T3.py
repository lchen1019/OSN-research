import utils
import GraphMaker as gm


# dfs标记，求出连通分量
def dfs(matrix, col, cnt, u, total_nodes):
    col[u - 1] = cnt
    for i in range(len(matrix)):
        if matrix[u - 1][i] == 'F' and col[i] == 0:
            total_nodes.remove(i + 1)
            dfs(matrix, col, cnt, i + 1, total_nodes)


def check(matrix):
    # 进行广度优先遍历
    queue = [0]
    n = len(matrix)
    col = [0 for i in range(n)]
    col[0] = 1
    while len(queue) > 0:
        u = queue[0]
        del queue[0]
        for v in range(n):
            if matrix[u][v] == 'E':
                if col[v] != 0:
                    if col[u] == col[v]:
                        return False
                else:
                    col[v] = 2 if col[u] == 1 else 1
                    queue.append(v)
    return True


def main():
    n = 15
    matrix = utils.get_polarized_network(n)
    # for i in matrix:
    #     print(i)
    edges = []
    for i in range(n):
        for j in range(i + 1):
            if matrix[i][j] != 'U':
                edges.append((i, j, matrix[i][j]))
    gm.paint_polarized(n, edges, '原始输入')
    # 求出所有连通分量
    total_nodes = {i + 1 for i in range(n)}
    col = [0 for i in range(n)]
    cnt = 1
    t = []
    while len(total_nodes) != 0:
        temp = total_nodes.copy()
        u = total_nodes.pop()
        dfs(matrix, col, cnt, u, total_nodes)
        t.append(temp.difference(total_nodes))
        cnt += 1
    print(col)
    print(cnt)
    print(t)
    cnt -= 1
    # 根据连通分量的关系，建立邻接矩阵
    matrix_after = [[0] * cnt for i in range(cnt)]
    for i in range(n):
        for j in range(n):
            if col[i] != col[j]:
                matrix_after[col[i] - 1][col[j] - 1] = matrix[i][j]
    for i in matrix_after:
        print(i)
    # 通过矩阵构建图
    edges = []
    for i in range(cnt):
        for j in range(cnt):
            if matrix_after[i][j] == 'E':
                edges.append((i, j))
    gm.paint(cnt, edges, "合并连通分支后的图")
    # 判断生成图是否为二分图，即可断定其稳定性
    if check(matrix_after):
        print("不包含包含奇数长度负圈，网络结构稳定")
    else:
        print("包含奇数长度负圈，网络结构不稳定")


if __name__ == "__main__":
    main()
