import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['STZhongsong']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def paint(data, col_names):
    print(col_names)
    print(['#FFFFFF'] * len(col_names))
    table = plt.table(cellText=data, colLabels=col_names, loc='center',
                      cellLoc='center', colColours=['#FFFFFF'] * len(col_names))
    table.auto_set_font_size(False)
    # h = table.get_celld()[(0, 0)].get_height()
    # w = table.get_celld()[(0, 0)].get_width()

    # Create an additional Header
    # header = [table.add_cell(-1, pos, w, h, loc="center", facecolor="none") for pos in [1, 2, 3]]
    # header[0].visible_edges = "TBL"
    # header[1].visible_edges = "TB"
    # header[2].visible_edges = "TBR"
    # header[1].get_text().set_text("Header Header Header Header")

    # plt.title("初始门槛值")
    plt.axis('off')
    plt.show()


# paint([[1, 2, 3, 4]], ['A'] * 4)
