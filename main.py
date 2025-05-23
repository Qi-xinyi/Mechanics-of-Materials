# 导入所需的模块
from pole import *  # 导入截面相关的类和函数
from force import *  # 导入力相关的类和函数
from check_equel import *  # 导入平衡检查相关的函数
from Torque import *  # 导入扭矩相关的类和函数
from σ import *  # 导入正应力计算相关的函数
from τ import *  # 导入切应力计算相关的函数
from torsion import *  # 导入扭转相关的函数

section = input(
    "请输入截面类型:\nHC空心圆柱\nH工型钢\nC圆柱\nSP弹簧\nQ矩形\nother其他\n"
)  # 获取用户输入的截面类型

if section == "Q":  # 如果选择矩形截面
    b = float(input("请输入矩形的宽度："))  # 获取矩形宽度
    h = float(input("请输入矩形的高度："))  # 获取矩形高度
    E = float(input("请输入材料的弹性模量："))  # 获取弹性模量
    G = float(input("请输入材料的剪切模量："))  # 获取剪切模量
    section1 = Q(b, h, E, G)
    # 创建矩形截面对象
if section == "H":  # 如果选择工型钢截面
    num = str(input("请输入工型钢的编号"))  # 获取工型钢编号
    E = float(input("请输入材料的弹性模量："))  # 获取弹性模量
    G = float(input("请输入材料的剪切模量："))  # 获取剪切模量
    section1 = H(num, E, G)  # 创建工型钢截面对象

if section == "HC":  # 如果选择空心圆柱截面
    De = float(input("请输入圆环的外径："))  # 获取圆环外径
    Di = float(input("请输入圆环的内径："))  # 获取圆环内径
    E = float(input("请输入材料的弹性模量："))  # 获取弹性模量
    G = float(input("请输入材料的剪切模量："))  # 获取剪切模量
    section1 = HC(De, Di, E, G)  # 创建空心圆柱截面对象

elif section == "other":  # 如果选择其他类型截面
    A = float(input("请输入截面的面积："))  # 获取截面面积
    E = float(input("请输入材料的弹性模量："))  # 获取弹性模量
    G = float(input("请输入材料的剪切模量："))  # 获取剪切模量
    section1 = other(A, E, G)  # 创建其他类型截面对象

elif section == "C":  # 如果选择实心圆柱截面
    D = float(input("请输入圆柱的直径："))  # 获取圆柱直径
    E = float(input("请输入材料的弹性模量："))  # 获取弹性模量
    G = float(input("请输入材料的剪切模量："))  # 获取剪切模量
    section1 = C(D, E, G)  # 创建实心圆柱截面对象

elif section == "SP":  # spring
    print("请输入弹簧的参数,如果参数为未知量则填写字母")
    try:
        D = float(input("请输入弹簧的直径："))
    except:
        D = "unknown"
    try:
        d = float(input("请输入弹簧的丝径："))
    except:
        d = "unknown"
    try:
        k = float(input("请输入弹簧的刚度："))
    except:
        k = "unknown"
    try:
        F = float(input("请输入弹簧的受力："))
    except:
        F = "unknown"
    shear_stress_max = float(input("请输入最大剪应力"))
    if D != "unknown" and d != "unknown" and k != "unknown" and F != "unknown":
        shear_stress = 8 * k * F * D / (pi * d**3)
        print(f"弹簧所受的切应力大小为{shear_stress:.2f}")
        if shear_stress <= shear_stress_max:
            print("弹簧满足要求")
        else:
            print("弹簧不满足要求，所需最大切应力至少为{shear_stress}")
    elif F == "unknown" and D != "unknown" and d != "unknown" and k != "unknown":
        F_max = shear_stress_max * pi * d**3 / (8 * D * k)
        print(f"弹簧最大可受力为{F_max}")
    elif d == "unknown":
        d_mini = 2 * (F * D * k / pi / shear_stress_max) ** (1 / 3)
        print(f"弹簧最小丝径为{d_mini}")
    else:
        print("不支持此类运算")
    exit(0)


length = float(input("请输入杆件的长度："))  # 获取杆件长度
maximum_shear_stress = float(input("请输入最大剪应力"))  # 获取材料允许的最大剪应力
Maximum_normal_stress = float(input("请输入最大正应力"))  # 获取材料允许的最大正应力


a3 = input("是否有.csv表格(y/n)")  # 询问是否从CSV文件导入力和力矩数据
if a3 == "y":  # 如果选择从CSV文件导入数据
    import pandas as pd  # 导入pandas库用于读取CSV文件

    # CSV文件格式说明：
    # type: 力的类型（'force' 或 'torque'）
    # position: 力的作用位置或力矩的作用位置
    # size: 力的大小或力矩的大小
    # direction: 力的方向或力矩的方向

    # 读取CSV文件
    df = pd.read_csv("force_and_torque.csv")

    # 初始化力和力矩的列表
    all_the_force = []  # 存储集中力
    all_the_force_continued = []  # 存储分布力
    all_the_torque = []  # 存储力矩

    # 处理CSV文件中的力数据
    for index, row in df[df["type"] == "force"].iterrows():  # 遍历所有类型为force的行
        position = row["position"]  # 获取力的作用位置
        size = row["size"]  # 获取力的大小
        direction = int(row["direction"])  # 获取力的方向

        if pd.isnull(position):  # 如果位置为空，则处理为分布力
            place_start = float(row["position_start"])  # 获取分布力起始位置
            place_end = float(row["position_end"])  # 获取分布力结束位置
            force1 = force_continued(
                length, place_start, place_end, size, direction
            )  # 创建分布力对象
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

    # 处理CSV文件中的力矩数据
    for index, row in df[df["type"] == "torque"].iterrows():  # 遍历所有类型为torque的行
        place = row["position"]  # 获取力矩作用位置
        size = row["size"]  # 获取力矩大小
        direction = int(row["direction"])  # 获取力矩方向
        torque1 = torque(length, place, size, direction)  # 创建力矩对象
        if torque1.check() == False:
            print(f"在索引{index}处的力矩作用位置超出杆件长度，已跳过")
            continue
        all_the_torque.append(torque1)

else:  # 如果选择手动输入数据
    all_the_force = []  # 初始化集中力列表
    all_the_force_continued = []  # 初始化分布力列表
    a = "y"  # 初始化循环控制变量
    while a == "y":  # 循环输入力的数据
        try:
            place = float(input("请输入力的作用位置（据起始点）(如为连续力输入c)："))
        except:
            place_start = float(input("请输入力的起始位置（据起始点）："))
            place_end = float(input("请输入力的结束位置（据起始点）："))
            size = float(input("请输入力的大小："))
            direction = int(input("请输入力的方向：（向上为“1”，向下为“2”）"))
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
        direction = int(
            input("请输入力矩的方向：（逆时针为1，顺时针为-1，向上为2，向下为-2）")
        )
        torque1 = torque(length, place, size, direction)
        if torque1.check() == False:
            print("力矩的作用位置超出杆件长度，请重新输入")
            continue
        all_the_torque = all_the_torque + [torque1]
        a = input("是否继续添加力矩(y/n)")

import os

a2 = "y"
while a2 != "n":
    os.system("cls" if os.name == "nt" else "clear")

    print("你想干什么")
    print("1.检查力平衡")
    print("2.检查力矩平衡")
    print("3.计算正应力（中心）")
    print("31.计算正应力（非中心且无轴向扭矩）")
    print("32.计算正应力（最大）")
    print("33.计算正应力（一根杆子上最大的正应力）")
    print("4.画出轴力图")
    print("5.画出正应力图（中心）")
    print("61.计算切应力(只有弯曲)")
    print("611.计算最大切应力(只有弯曲)")
    print("62.计算切应力(只有扭转)")
    print("621.计算最大切应力(只有扭转)")
    print("7.计算弯力")
    print("8.计算弯矩")
    print("9.画弯力图")
    print("10.画弯矩图")
    print("11.计算扭矩")
    print("12.画出扭矩图")
    print("13.测试")

    choice = str(input("请输入你的选择："))

    if choice == "1":
        check_force_equal(all_the_force, all_the_force_continued)

    elif choice == "2":
        check_torsque_equal(all_the_force, all_the_force_continued, all_the_torque)

    elif choice == "3":
        x = float(input("请输入计算点的位置："))
        try:
            A = section1.A
        except:
            print("未存取截面面积")
            A = float(input("请输入截面面积："))
        σ = normal_stress(all_the_force, x, section1.A, Maximum_normal_stress)
        if σ > Maximum_normal_stress:
            print("截面上{x}处的正应力超过了材料的最大承受应力")

    elif choice == "31":
        try:
            A = section1.A
        except:
            print("未存取截面面积")
            A = float(input("请输入截面面积："))
        try:
            I_z = section1.I_z
        except:
            print("未存取截面惯性矩")
            I_z = float(input("请输入截面惯性矩："))
        y = float(input("请输入计算点到中心的距离："))
        x = float(input("请输入计算点的位置："))
        σ = (
            normal_stress(all_the_force, 0, section1.A, Maximum_normal_stress, 0)
            + torque_s(x, all_the_force, all_the_force_continued, all_the_torque, 0)
            * y
            / I_z
        )

    elif choice == "32":
        try:
            A = section1.A
        except:
            print("未存取截面面积")
            A = float(input("请输入截面面积："))
        try:
            W_z = section1.W_z
        except:
            print("未存取截面惯性矩")
            W_z = float(input("请输入截面惯性矩："))
        x = float(input("请输入计算点的位置："))
        σ = (
            normal_stress(all_the_force, 0, section1.A, Maximum_normal_stress, 0)
            + torque_s(x, all_the_force, all_the_force_continued, all_the_torque, 0)
            / W_z
        )
        if σ > Maximum_normal_stress:
            print(f"截面上{x}处的正应力的大小为{σ}超过了材料的最大承受应力")
        else:
            print(f"截面上{x}处的正应力的大小为{σ}未超过材料的最大承受应力")

    elif choice == "33":
        try:
            A = section1.A
        except:
            print("未存取截面面积")
            A = float(input("请输入截面面积："))
        try:
            y_max = section1.y_max
        except:
            print("未存取截面最大y坐标")
            y_max = float(input("请输入截面最大y坐标："))
        try:
            W_z = section1.W_z
        except:
            print("未存取截面惯性矩")
            W_z = float(input("请输入截面惯性矩："))
        σ_max = 0
        for x in np.arange(0, length, 0.1):
            σ = (
                normal_stress(all_the_force, 0, section1.A, Maximum_normal_stress, 0)
                + torque_s(x, all_the_force, all_the_force_continued, all_the_torque, 0)
                / W_z
            )
            if σ > σ_max:
                σ_max = σ
        if σ_max > Maximum_normal_stress:
            print(f"截面上某处的有最大正应力为{σ_max}超过了材料的最大承受应力")
        else:
            print(f"截面上某处的有最大正应力为{σ_max}未超过材料的最大承受应力")

    elif choice == "4":
        paint_normal_force(all_the_force, length, section1.A)

    elif choice == "5":
        paint_normal_stress(all_the_force, length, section1.A)

    elif choice == "7":
        x = float(input("请输入计算点的位置："))
        answer = cacular_force_s(all_the_force, all_the_force_continued, x)
        print(f"在{x}处，该杆件的弯力为{answer}")

    elif choice == "8":
        x = float(input("请输入计算点的位置："))
        answer = torque_s(x, all_the_force, all_the_force_continued, all_the_torque)
        print(f"在{x}处，该杆件的弯矩为{answer}")

    elif choice == "9":
        paint_force_s(all_the_force, all_the_force_continued, length)

    elif choice == "10":
        paint_torque_s(length, all_the_force, all_the_force_continued, all_the_torque)

    elif choice == "11":
        x = float(input("请输入计算点的位置："))
        answer = calcular_torsion(all_the_torque, x)
        print(f"在{x}处，该杆件的扭矩为{answer}")

    elif choice == "12":
        paint_torsion(all_the_torque, length)

    elif choice == "61":
        x = float(input("请输入计算点的位置："))
        answer = shear_stress(all_the_force, y, section1, all_the_force_continued, x)
        print(f"在{x}处，且距离中心{y}处，该杆件的切应力为{answer}")

    elif choice == "611":
        try:
            y_max = section1.y_max
        except:
            print("未存取截面最大y坐标")
            y_max = float(input("请输入截面最大y坐标："))
            τ_max = 0
        for x in np.arange(0, length, 0.1):
            τ = shear_stress(all_the_force, y_max, section1, all_the_force_continued, x)
            if τ > τ_max:
                τ_max = τ
        if τ_max > maximum_shear_stress:
            print(f"截面上某处的有最大切应力为{τ_max}超过了材料的最大承受应力")
        else:
            print(f"截面上某处的有最大切应力为{τ_max}未超过材料的最大承受应力")

    elif choice == "62":
        x = float(input("请输入计算点的位置："))
        y = float(input("请输入计算点距几何中心的距离："))
        answer = shear_stress_torsion(all_the_torque, I_p, x, y)
        print(f"在{x}处，该杆件的转动惯量为{answer}")

    elif choice == "621":
        try:
            y_max = section1.y_max
        except:
            print("未存取截面最大y坐标")
            y_max = float(input("请输入截面最大y坐标："))
        try:
            I_p = section1.I_p
        except:
            print("未存取截面转动惯量")
            I_p = float(input("请输入截面转动惯量："))
        τ_max = 0
        for x in np.arange(0, length, 0.1):
            τ = shear_stress_torsion(all_the_torque, I_p, x, y_max, 0)
            if τ > τ_max:
                τ_max = τ
        if τ_max > maximum_shear_stress:
            print(f"截面上某处的有最大切应力为{τ_max}超过了材料的最大承受应力")
        else:
            print(f"截面上某处的有最大切应力为{τ_max}未超过材料的最大承受应力")

    elif choice == "13":
        try:
            A = section1.A
            print(f"A={section1.A}")
        except:
            print("未存取截面面积")
        try:
            I_z = section1.I_z
            print(f"I_z={section1.I_z}")
        except:
            print("未存取截面惯性矩")
        try:
            y_max = section1.y_max
            print(f"y_max={section1.y_max}")
        except:
            print("未存取截面最大y坐标")
        try:
            W_z = section1.W_z
            print(f"W_z={section1.W_z}")
        except:
            print("未存取截面重心")

    else:
        print("功能未开发")

    a2 = input("是否继续操作(y/n)")
