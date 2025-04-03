import matplotlib.pyplot as plt


# σ
def normal_stress(all_the_force, x, A, max, t=1):
    """
    计算指定截面上某点的正应力。

    Args:
        all_the_force (list): 力的列表，其中每个元素是一个包含力的大小、方向和作用位置的力的对象。
        x (float): 需要计算正应力的截面的位置。
        A (float): 截面的面积。
        max (float): 力的最大值，用于确定力的方向。
        t (int, optional): 是否打印计算结果，默认为0（不打印）。

    Returns:
        float: 指定截面上某点的正应力。

    """
    force_left = 0
    force_right = 0
    for force in all_the_force:
        if force.place < x:
            if force.direction == 3:
                force_left += force.size
            elif force.direction == 4:
                force_right += force.size
        else:
            continue
    force_add = force_right - force_left
    σ = force_add / A
    if t == 1:
        print(f"截面上{x}处的正应力为{σ}")
    return σ


import matplotlib.pyplot as plt


def paint_normal_force(all_the_force, x, A):
    """
    根据给定的力和横截面积绘制正压力图。

    Args:
        all_the_force (float): 总力，单位：牛顿（N）。
        x (float): 横坐标的最大值，单位：米（m）。
        A (float): 横截面积，单位：平方米（m^2）。

    Returns:
        None

    """
    # 生成数据点
    step = max(1, int(x / 100))
    x_values = range(0, int(x), step)
    y_values_A = [normal_stress(all_the_force, place, A, max, 1) for place in x_values]
    y_values = [value * A for value in y_values_A]

    # 绘制函数图
    plt.plot(x_values, y_values)

    # 添加标题和标签
    plt.title("F_n")
    plt.xlabel("x/m")
    plt.ylabel("F_n/N")

    # 显示图形
    plt.show()


def paint_normal_stress(all_the_force, x, A):
    """
    绘制正应力图。

    Args:
        all_the_force (float): 所有作用在物体上的力之和，单位牛顿（N）。
        x (float): 物体长度，单位米（m）。
        A (float): 物体横截面积，单位平方米（m^2）。

    Returns:
        正应力图

    """
    # 生成数据点
    step = max(1, int(x / 100))
    x_values = range(0, int(x), step)
    y_values = [normal_stress(all_the_force, place, A, max, 1) for place in x_values]

    # 绘制函数图
    plt.plot(x_values, y_values)

    # 添加标题和标签
    plt.title("σ")
    plt.xlabel("x/m")
    plt.ylabel("σ/Pa")

    # 显示图形
    plt.show()
