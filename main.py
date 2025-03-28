from pole import *
from force import *
from check_equel import *
from Torque import *
from σ import *
from τ import *
from torsion import *

section = input("请输入截面类型：(HC空心圆柱,other其他)")  # 获取用户输入的截面类型

if section == "HC":
    De = float(input("请输入圆环的外径："))
    Di = float(input("请输入圆环的内径："))
    E = float(input("请输入材料的弹性模量："))
    G = float(input("请输入材料的剪切模量："))
    section1 = HC(De, Di, E, G)
    print(f"圆环截面的惯性矩为：{section1.I_z}")
    print(f"圆环截面的极惯性矩为：{section1.I_p}")
    print(f"圆环截面的抗扭截面模量为：{section1.W_t}")
    print(f"圆环截面的面积为：{section1.A}")

elif section == "other":
    A = float(input("请输入截面的面积："))
    I_z = float(input("请输入截面的惯性矩："))
    E = float(input("请输入材料的弹性模量："))
    G = float(input("请输入材料的剪切模量："))
    I_p = float(input("请输入截面的极惯性矩："))
    W_t = float(input("请输入截面的抗扭截面模量："))
    sectio1 = other(A, E, G, I_z, W_t, I_p)  # 创建其他类型截面对象

length = float(input("请输入杆件的长度："))  # 后期将这些特征与pole类的属性联系起来
maximum_shear_stress = float(input("请输入最大剪应力"))
Maximum_normal_stress = float(input("请输入最大正应力"))


a3 = input("是否有.csv表格(y/n)")
if a3 == "y":
    import pandas as pd

    # 假设CSV文件名为forces_and_torques.csv，并且具有以下列：
    # type: 力的类型（'force' 或 'torque'）
    # position: 力的作用位置或力矩的作用位置
    # size: 力的大小或力矩的大小
    # direction: 力的方向或力矩的方向

    # 读取CSV文件
    df = pd.read_csv("D:\\材料力学\\程序\\luoyining.csv")

    all_the_force = []
    all_the_force_continued = []
    all_the_torque = []

    # 处理力
    for index, row in df[df["type"] == "force"].iterrows():
        position = row["position"]
        size = row["size"]
        direction = str(row["direction"])

        if pd.isnull(position):  # 如果位置为空，则处理为连续力
            place_start = float(row["position_start"])
            place_end = float(row["position_end"])
            force1 = force_continued(length, place_start, place_end, size, direction)
            if force1.check() == False:
                print(f"在索引{index}处的力的作用位置超出杆件长度，已跳过")
                continue
            all_the_force_continued.append(force1)
        else:
            force1 = force(length, position, size, direction)
            if force1.check() == False:
                print(f"在索引{index}处的力的作用位置超出杆件长度，已跳过")
                continue
            all_the_force.append(force1)

    # 处理力矩
    for index, row in df[df["type"] == "torque"].iterrows():
        place = row["position"]
        size = row["size"]
        direction = row["direction"]

        torque1 = torque(length, place, size, direction)
        if torque1.check() == False:
            print(f"在索引{index}处的力矩作用位置超出杆件长度，已跳过")
            continue
        all_the_torque.append(torque1)

else:
    all_the_force = []
    all_the_force_continued = []
    a = "y"
    while a == "y":
        try:
            place = float(input("请输入力的作用位置（据起始点）(如为连续力输入c)："))
        except:
            place_start = float(input("请输入力的起始位置（据起始点）："))
            place_end = float(input("请输入力的结束位置（据起始点）："))
            size = float(input("请输入力的大小："))
            direction = input("请输入力的方向：（向上为“1”，向下为“2”）")
            force1 = force_continued(length, place_start, place_end, size, direction)
            if force1.check() == False:
                print("力的作用位置超出杆件长度，请重新输入")
                continue
            all_the_force_continued = all_the_force_continued + [force1]
            a = input("是否继续添加力(y/n)")
            continue
        size = float(input("请输入力的大小："))
        direction = input(
            "请输入力的方向：（向上为“1”，向下为“2”，向左为“3”，向右为“4”）"
        )
        force1 = force(length, place, size, direction)
        if force1.check() == False:
            print("力的作用位置超出杆件长度，请重新输入")
            continue
        all_the_force = all_the_force + [force1]
        a = input("是否继续添加力(y/n)")

    all_the_torque = []
    a = input("是否继续添加力矩(y/n)")
    while a == "y":
        place = float(input("请输入力矩的作用位置（据起始点）："))
        size = float(input("请输入力矩的大小："))
        direction = input("请输入力矩的方向：（顺时针为“-1”，逆时针为“1”）")
        torque1 = torque(length, place, size, direction)
        if torque1.check() == False:
            print("力矩的作用位置超出杆件长度，请重新输入")
            continue
        all_the_torque = all_the_torque + [torque1]
        a = input("是否继续添加力矩(y/n)")

import os

a2 = "y"
while a2 == "y":
    os.system("cls" if os.name == "nt" else "clear")

    print("你想干什么")
    print("1.检查力平衡")
    print("2.检查力矩平衡")
    print("3.计算正应力（中心）")
    print("4.画出轴力图")
    print("5.画出正应力图（中心）")
    print("6.计算切应力")
    print("7.计算弯力")
    print("8.计算弯矩")
    print("9.画弯力图")
    print("10.画弯矩图")
    print("11.计算扭矩")
    print("12.画出扭矩图")

    choice = int(input("请输入你的选择："))
    if choice == "1":
        check_force_equal(all_the_force, all_the_force_continued)

    elif choice == "2":
        check_torsque_equal(all_the_force, all_the_force_continued, all_the_torque)

    elif choice == "3":
        x = float(input("请输入计算点的位置："))
        σ = normal_stress(all_the_force, x, section1.A, Maximum_normal_stress)
        if σ > Maximum_normal_stress:
            print("截面上{x}处的正应力超过了材料的最大承受应力")

    elif choice == "4":
        paint_normal_force(all_the_force, length, section1.A)

    elif choice == "5":
        paint_normal_stress(all_the_force, length, section1.A)

    elif choice == "6":
        x = float(input("请输入计算点的位置："))
        shear_stress(all_the_force, x, section1.A, maximum_shear_stress)

    elif choice == "7":
        x = float(input("请输入计算点的位置："))
        cacular_force_s(all_the_force, all_the_force_continued, x)

    elif choice == "8":
        x = float(input("请输入计算点的位置："))
        torque_s(x, all_the_force, all_the_force_continued, all_the_torque)

    elif choice == "9":
        paint_force_s(all_the_force, all_the_force_continued, length)

    elif choice == "10":
        paint_torque_s(all_the_torque, length)

    elif choice == "11":
        x = float(input("请输入计算点的位置："))
        calcular_torsion(all_the_torque, x)

    elif choice == "12":
        paint_torsion(all_the_torque, length)

    else:
        print("功能未开发")

    a2 = input("是否继续操作(y/n)")
