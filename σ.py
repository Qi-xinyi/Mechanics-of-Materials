import matplotlib.pyplot as plt


# σ
def normal_stress(all_the_force, x, A, max, t=0):
    force_left = 0
    force_right = 0
    for force in all_the_force:
        if force.place < x:
            if force.direction == "3":
                force_left += force.size
            elif force.direction == "4":
                force_right += force.size
        else:
            continue
    force_add = force_right - force_left
    σ = force_add / A
    if t == 0:
        print(f"截面上{x}处的正应力为{σ}")
    return σ


import matplotlib.pyplot as plt


def paint_normal_force(all_the_force, x, A):
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
