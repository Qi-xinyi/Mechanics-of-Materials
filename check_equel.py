from force import force


def check_force_equal(all_the_force, all_the_force_continued):
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
    检查转动惯量是否平衡。

    Args:
        all_the_force (list): 力的列表，每个元素包含大小（size）、方向（direction）和作用位置（place）。
        all_the_force_continued (list): 持续作用力的列表，每个元素包含大小（size）、方向（direction）、起始作用位置（place_start）和终止作用位置（place_end）。
        all_the_torque (list): 扭矩的列表，每个元素包含大小（size）和方向（direction）。

    Returns:
        bool: 如果转动惯量平衡，则返回True；否则返回False。

    """
    c = "转动惯量不平衡"

    torque_left = 0
    torque_right = 0
    for force in all_the_force:
        if force.direction == 1:
            torque_ni += force.size * force.place
        elif force.direction == 2:
            torque_shun += force.size * force.place
    for torque in all_the_torque:
        if torque.direction == 1:
            torque_left += torque.size
        elif torque.direction == -1:
            torque_right += torque.size
    for force in all_the_force_continued:

        if force.direction == 1:
            torque_ni += force.size * ((force.place_end**2 - force.place_start**2) / 2)
        elif force.direction == 2:
            torque_shun += force.size * (
                (force.place_end**2 - force.place_start**2) / 2
            )

    if abs(torque_left - torque_right) > 0.001:
        c = c + a
    if c != "":
        print(c)
        return False
    else:
        print("转动惯量平衡")
        return True
