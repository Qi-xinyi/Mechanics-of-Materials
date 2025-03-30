import matplotlib.pyplot as plt
import numpy as np


class force:
    def __init__(self, long, place, size, direction):
        self.long = long
        self.size = size
        self.direction = direction
        self.place = place

    def check(self):
        if self.place > self.long or self.place < 0:
            return False
        else:
            return True


class force_continued:
    def __init__(self, long, place_start, place_end, size, direction):
        self.long = long
        self.size = size
        self.direction = direction  # 1为向上，2为向下,3为向左，4为向右
        self.place_start = place_start
        self.place_end = place_end

    def check(self):
        if self.place_end > self.long or self.place_start < 0:
            return False
        else:
            return True


def cacular_force_s(all_the_force, all_the_force_continued, s, a=1):
    """
    计算位置s处的合力

    Args:
        all_the_force (list): 瞬时力列表，每个元素是一个包含力的属性（位置、方向、大小）的对象
        all_the_force_continued (list): 持续力列表，每个元素是一个包含力的属性（起始位置、结束位置、方向、大小）的对象
        s (float): 计算合力的位置
        a (int, optional): 打印结果的开关，默认为1表示打印，0表示不打印。默认为1。

    Returns:
        float: 位置s处的合力大小
    """
    force_up = 0
    force_down = 0
    for force1 in all_the_force:
        if force1.place < s:
            if force1.direction == 1:
                force_up += force1.size
            elif force1.direction == 2:
                force_down += force1.size
    for force1 in all_the_force_continued:
        if force1.place_end <= s:
            if force1.direction == 1:
                force_up += force1.size * (force1.place_end - force1.place_start)
            elif force1.direction == 2:
                force_down += force1.size * (force1.place_end - force1.place_start)
        elif force1.place_start < s and force1.place_end > s:
            if force1.direction == 1:
                force_up += force1.size * (s - force1.place_start)
            elif force1.direction == 2:
                force_down += force1.size * (s - force1.place_start)
    F_s = force_up - force_down
    if a == 1:
        print(f"F_s at {s} is {F_s} N")
    return F_s


def paint_force_s(all_the_force, all_the_force_continued, length):
    """
    绘制力F_s随位置变化的函数图。

    Args:
        all_the_force (list): 所有的力值列表。
        all_the_force_continued (list): 所有力的持续状态列表。
        length (float): 绘制图形的总长度，单位：米。

    Returns:
        None

    """
    # 生成数据点
    step = length / 1000
    x_values = np.arange(0, length + step, step)
    y_values = [
        cacular_force_s(all_the_force, all_the_force_continued, place, 0)
        for place in x_values
    ]

    # 绘制函数图
    plt.plot(x_values, y_values)

    # 添加标题和标签
    plt.title("F_s")
    plt.xlabel("x/m")
    plt.ylabel("F_s/N")

    # 显示图形
    plt.show()
