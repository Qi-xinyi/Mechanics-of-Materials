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
            if force1.direction == "1":
                force_up += force1.size
            elif force1.direction == "2":
                force_down += force1.size
    for force1 in all_the_force_continued:
        if force1.place_end <= s:
            if force1.direction == "1":
                force_up += force1.size * (force1.place_end - force1.place_start)
            elif force1.direction == "2":
                force_down += force1.size * (force1.place_end - force1.place_start)
        elif force1.place_start < s and force1.place_end > s:
            if force1.direction == "1":
                force_up += force1.size * (s - force1.place_start)
            elif force1.direction == "2":
                force_down += force1.size * (s - force1.place_start)
    F_s = force_up - force_down
    if a == 1:
        print(f"F_s at {s} is {F_s} N")
    return F_s


def torque_s(s, all_the_force, all_the_force_continued, all_the_torque, a=1):
    """
    计算s位置处的扭矩。

    Args:
        s (float): 计算扭矩的位置。
        all_the_force (list): 静态力的列表，每个力由包含以下属性的对象表示：
            - place (float): 力的作用位置。
            - direction (str): 力的方向，"1"表示向上，"2"表示向下。
            - size (float): 力的大小。
        all_the_force_continued (list): 持续力的列表，每个力由包含以下属性的对象表示：
            - place_start (float): 力的起始作用位置。
            - place_end (float): 力的终止作用位置。
            - direction (str): 力的方向，"1"表示向上，"2"表示向下。
            - size (float): 力的大小。
        all_the_torque (list): 扭矩的列表，每个扭矩由包含以下属性的对象表示：
            - place (float): 扭矩的作用位置。
            - direction (str): 扭矩的方向，"1"表示顺时针方向（对应向下的扭矩），"-1"表示逆时针方向（对应向上的扭矩）。
            - size (float): 扭矩的大小。
        a (int, optional): 打印输出标志，默认为1。如果为1，则打印计算结果。Defaults to 1.

    Returns:
        float: s位置处的扭矩。

    """
    torque_up = 0
    torque_down = 0

    for force1 in all_the_force:
        if force1.place <= s:
            if force1.direction == "1":
                torque_up += force1.size * force1.place
            elif force1.direction == "2":
                torque_down += force1.size * force1.place

    for force1 in all_the_force_continued:
        if force1.place_end <= s:
            if force1.direction == "1":
                torque_up += (
                    force1.size * (force1.place_end**2 - force1.place_start**2) / 2
                )
                torque_down += (
                    force1.size * (force1.place_end**2 - force1.place_start**2) / 2
                )
        elif force1.place_start < s and force1.place_end > s:
            if force1.direction == "1":
                torque_up += force1.size * (s**2 - force1.place_start**2) / 2
            elif force1.direction == "2":
                torque_down += force1.size * (s**2 - force1.place_start**2) / 2

    for torque1 in all_the_torque:
        if torque1.place <= s:
            if torque1.direction == "1":
                torque_down += torque1.size
            elif torque1.direction == "-1":
                torque_up += torque1.size
    M = torque_up - torque_down
    if a == 1:
        print(f"M_s at {s} is {M} N*m")
    return M


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
    x_values = np.arange(0, length, step)
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


def paint_torque_s(length, all_the_force, all_the_force_continued, all_the_torque):
    """
    绘制力矩M_s随位置变化的函数图。

    Args:
        length (float): 总长度，单位米。
        all_the_force (float): 总力，单位牛顿。
        all_the_force_continued (float): 继续的总力，单位牛顿。
        all_the_torque (float): 总力矩，单位牛顿米。

    Returns:
        None

    """
    # 生成数据点
    step = length / 1000
    x_values = np.arange(0, length, step)
    y_values = [
        torque_s(place, all_the_force, all_the_force_continued, all_the_torque, 0)
        for place in x_values
    ]

    # 绘制函数图
    plt.plot(x_values, y_values)

    # 添加标题和标签
    plt.title("M_s")
    plt.xlabel("x/m")
    plt.ylabel("M_s/N")

    # 显示图形
    plt.show()
