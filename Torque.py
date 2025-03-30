import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy import integrate
from force import cacular_force_s


class torque:
    def __init__(self, long, place, size, direction):
        self.long = long
        self.place = place
        self.size = size
        self.direction = direction  # 逆时针为1，顺时针为-1，向上为2，向下为-2

    def check(self):
        if self.place > self.long or self.place < 0:
            return False
        else:
            return True


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

    def force_s_func(s):
        return cacular_force_s(all_the_force, all_the_force_continued, s, 0)

    torque_up, a = integrate.quad(force_s_func, 0, s)

    for torque1 in all_the_torque:
        if torque1.place <= s:
            if torque1.direction == 1:
                torque_down += torque1.size
            elif torque1.direction == -1:
                torque_up += torque1.size
    M = torque_up - torque_down
    if a == 1:
        print(f"M_s at {s} is {M} N*m")
    return M


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
    x_values = np.arange(0, length + 2 * step, step)
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
