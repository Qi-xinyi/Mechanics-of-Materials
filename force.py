import matplotlib.pyplot as plt


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


def cacular_force_s(all_the_force, all_the_force_continued, s):
    """_summary_

    Args:
        all_the_force (_type_): _description_
        all_the_force_continued (_type_): _description_
        s (_type_): _description_
    """
    for force1 in all_the_force:
        if force1.place < s:
            if force1.direction == "1":
                force_up += force1.size
            elif force1.direction == "2":
                force_down += force1.size
    for force1 in all_the_force_continued:
        if force1.place_end < s:
            if force1.direction == "1":
                force_up += force1.size * (force1.place_end - force1.place_start)
            elif force1.direction == "2":
                force_down += force.size * (force1.place_end - force1.place_start)
        elif force1.place_start < s and force1.place_end > s:
            if force1.direction == "1":
                force_up += force1.size * (s - force1.place_start)
            elif force1.direction == "2":
                force_down += force1.size * (s - force1.place_start)
    F_s = force_up - force_down
    return F_s


def torque_s(s, all_the_force, all_the_force_continued, all_the_torque):
    for force1 in all_the_force:
        if force1.place < s:
            if force1.direction == "1":
                torque_up += force1.size * force1.place
            elif force1.direction == "2":
                torque_down += force1.size * force1.place

    for force1 in all_the_force_continued:
        if force1.place_end < s:
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
        if torque1.place < s:
            if torque1.direction == "1":
                torque_down += torque1.size
            elif torque1.direction == "-1":
                torque_up += torque1.size
    M = torque_up - torque_down
    return M


def paint_force_s(all_the_force, all_the_force_continued, length):
    # 生成数据点
    step = max(1, int(length / 1000))
    x_values = range(0, int(length), step)
    y_values = [
        cacular_force_s(all_the_force, all_the_force_continued, place)
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
    # 生成数据点
    step = max(1, int(length / 1000))
    x_values = range(0, int(length), step)
    y_values = [
        cacular_force_s(all_the_force, all_the_force_continued, place)
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
