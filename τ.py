from math import *
from force import cacular_force_s
from torsion import calcular_torsion

# def shear_stress_curved(all_the_force, all_the_force_contitued, x, A, a=1):
#     F_s=cacular_force_s(all_the_force, all_the_force_contitued, x,0)
#     τ=F_s*S_z/A/
#     return τ


def S_z(y, A):
    """
    计算截面上某点的剪应力。

    Args:
        y (float): 截面上某点到中性轴的距离。
        A (float): 截面的面积。

    Returns:
        float: 截面上某点的剪应力。

    """
    return y / A


def shear_stress_torsion(all_the_torque, I_p, x, y, a=1):
    T = calcular_torsion(all_the_torque, x)
    τ = T * y / I_p
    if a == 1:
        print(f"纯扭转情况下切应力的大小为{τ}")
    return τ


def shear_stress(all_the_force, y, section1, all_the_force_continued, x):
    try:
        S_z = S_z(y)
    except:
        print("未存取截面剪应力")
        S_z = float(input("请输入截面剪应力："))
    try:
        b = section1.b1(y)
    except:
        print("未存取截面宽度")
        b = float(input("请输入截面宽度："))
    F_s = cacular_force_s(all_the_force, all_the_force_continued, x)
    try:
        I_z = section1.I_z
    except:
        print("未存取截面惯性矩")
        I_z = float(input("请输入截面惯性矩："))
    return F_s * S_z / b / I_z
