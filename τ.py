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
