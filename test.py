import networkx as nx
import matplotlib.pyplot as plt


def main():
    G = nx.DiGraph()
    # 添加对应的边和点
    for i in range(1, 10):
        G.add_node(i, desc=str(i))
    G.add_edge(1, 2, name='6')
    G.add_edge(1, 3, name='4')
    G.add_edge(1, 4, name='5')
    G.add_edge(2, 5, name='1')
    G.add_edge(3, 5, name='1')
    G.add_edge(4, 6, name='2')
    G.add_edge(5, 7, name='9')
    G.add_edge(5, 8, name='7')
    G.add_edge(6, 8, name='4')
    G.add_edge(7, 9, name='2')
    G.add_edge(8, 9, name='4')

    # 按pos所定位置画出节点,无标签无权值，有多种layout
    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos, with_labels=None)
    # 画出标签
    node_labels = nx.get_node_attributes(G, 'desc')
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    # 画出边权值
    # edge_labels = nx.get_edge_attributes(G, 'name')
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title('AOE_CPM', fontsize=10)
    plt.show()


if __name__ == '__main__':
    main()
