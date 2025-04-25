import matplotlib.pyplot as plt
import numpy as np


def calcular_torsion(all_the_torique, x):
    """
    计算指定位置x的扭转力。

    Args:
        all_the_torique (list): 包含所有扭距的列表，每个元素为一个Torique对象。
        x (float): 需要计算扭转力的位置。

    Returns:
        float: 位置x处的扭转力。

    """
    torique_up = 0
    torique_down = 0
    for torique1 in all_the_torique:
        if torique1.place < x:
            if torique1.direction == 2:
                torique_up += torique1.size
            elif torique1.direction == -2:
                torique_down += torique1.size

    torsion = torique_up - torique_down
    return torsion


def paint_torsion(all_the_torique, length):
    """
    绘制扭矩曲线图。

    Args:
        all_the_torique (list): 包含扭矩值的列表。
        length (float):杆的长度，单位为米。

    Returns:
        None


    """
    step = length / 1000
    x_values = np.arange(0, length + 2 * step, step)
    y_values = [calcular_torsion(all_the_torique, place) for place in x_values]

    # 绘制函数图
    plt.plot(x_values, y_values)

    # 添加标题和标签
    plt.title("T")
    plt.xlabel("x/m")
    plt.ylabel("T/N*m")

    # 显示图形
    plt.show()
