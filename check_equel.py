from force import force


def check_force_equal(all_the_force, all_the_force_continued):
    """
    检查所有力是否平衡。

    Args:
        all_the_force (list): 包含力的列表，每个力是一个对象，包含大小（size）、方向（direction）和起始位置（place_start）和结束位置（place_end）。
        all_the_force_continued (list): 包含持续力的列表，每个力是一个对象，包含大小（size）、方向（direction）和起始位置（place_start）和结束位置（place_end）。

    Returns:
        bool: 如果所有力平衡，则返回True；否则返回False。

    """
    a = " 上下方向的力不平衡 "
    b = " 左右方向的力不平衡 "
    c = ""
    force_up = 0
    force_down = 0
    force_left = 0
    force_right = 0
    for force in all_the_force_continued:
        if force.direction == "1":
            force_up += force.size * (force.place_end - force.place_start)
        elif force.direction == "2":
            force_down += force.size * (force.place_end - force.place_start)
    for force in all_the_force:
        if force.direction == "1":
            force_up += force.size
        elif force.direction == "2":
            force_down += force.size
        elif force.direction == "3":
            force_left += force.size
        elif force.direction == "4":
            force_right += force.size
    if abs(force_up - force_down) > 0.001:
        c = c + a
    if abs(force_left - force_right) > 0.001:
        c = c + b
    if c != "":
        print(c)
        return False
    else:
        print("力平衡")
        return True


def check_torsque_equal(all_the_force, all_the_force_continued, all_the_torque):
    """
    检查法向和轴向转动惯量是否平衡。

    Args:
        all_the_force (list): 包含所有作用力的列表，每个作用力是包含方向（direction）、大小（size）和作用位置（place）的字典。
        all_the_force_continued (list): 包含所有持续作用力的列表，每个持续作用力是包含方向（direction）、大小（size）、起始作用位置（place_start）和结束作用位置（place_end）的字典。
        all_the_torque (list): 包含所有扭矩的列表，每个扭矩是包含方向（direction）和大小（size）的字典。

    Returns:
        bool: 如果法向和轴向转动惯量都平衡，返回True；否则返回False。

    """
    # 定义错误信息的字符串
    a = " 法向扭矩不平衡 "
    b = " 轴向扭矩不平衡 "
    c = ""

    # 初始化扭矩变量
    torque_ni = 0
    torque_shun = 0
    torque_up = 0
    torque_down = 0

    # 计算法向扭矩
    for force in all_the_force:
        if force.direction == 1:
            # 计算左向法向扭矩
            torque_ni += force.size * force.place
        elif force.direction == 2:
            # 计算右向法向扭矩
            torque_shun += force.size * force.place

    # 计算轴向扭矩
    for torque in all_the_torque:
        if torque.direction == 1:
            # 计算右向轴向扭矩
            torque_ni += torque.size
        elif torque.direction == -1:
            # 计算左向轴向扭矩
            torque_shun += torque.size
        elif torque.direction == 2:
            # 计算上向轴向扭矩
            torque_up += torque.size
        elif torque.direction == -2:
            # 计算下向轴向扭矩
            torque_down += torque.size

    # 计算持续力的法向扭矩
    for force in all_the_force_continued:
        if force.direction == 1:
            # 计算左向法向扭矩（持续力）
            torque_ni += force.size * ((force.place_end**2 - force.place_start**2) / 2)
        elif force.direction == 2:
            # 计算右向法向扭矩（持续力）
            torque_shun += force.size * (
                (force.place_end**2 - force.place_start**2) / 2
            )

    # 判断轴向转动惯量是否平衡
    if abs(torque_up - torque_down) > 0.001:
        c = c + b

    # 判断法向转动惯量是否平衡
    if abs(torque_shun - torque_ni) > 0.001:
        c = c + a

    # 输出结果并返回是否平衡
    if c != "":
        print(c)
        return False
    else:
        print("转动惯量平衡")
        return True
