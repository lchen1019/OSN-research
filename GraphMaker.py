import networkx as nx
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['STZhongsong']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def paint(nodes_number, edges, name):
    G = nx.Graph()
    # 添加对应的边和点
    for i in range(1, nodes_number):
        G.add_node(i, desc=str(i))
    # 两种方式加边，一种可以指明name
    # G.add_edge(1, 2, name='6')
    G.add_edges_from(edges)
    # 按pos所定位置画出节点,无标签无权值，有多种layout
    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos, with_labels=None)
    # 画出标签
    node_labels = nx.get_node_attributes(G, 'desc')
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    # 画出边权值
    # edge_labels = nx.get_edge_attributes(G, 'name')
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(name, fontsize=10)
    plt.show()


def paint_polarized(nodes_number, edges, name):
    G = nx.Graph()
    # 添加对应的边和点
    for i in range(1, nodes_number):
        G.add_node(i, desc=str(i))
    # 两种方式加边，一种可以指明name
    for edge in edges:
        G.add_edge(edge[0], edge[1], name=edge[2])
    # 按pos所定位置画出节点,无标签无权值，有多种layout
    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos, with_labels=None)
    # 画出标签
    node_labels = nx.get_node_attributes(G, 'desc')
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    # 画出边权值
    edge_labels = nx.get_edge_attributes(G, 'name')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(name, fontsize=10)
    plt.show()


# demo
def main():
    edges = [
        (1, 2),
        (2, 3),
        (3, 4),
        (1, 5),
        (2, 7),
        (3, 6),
        (4, 5)
    ]
    paint(7, edges, '合并连通分支后的图')


if __name__ == '__main__':
    main()
