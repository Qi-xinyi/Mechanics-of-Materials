from math import *


class section:
    """
    初始化函数。

    Args:
        E (float): 参数E的值。
        G (float): 参数G的值。

    """

    def __init__(self, E, G):
        # 初始化属性E
        self.E = E
        # 初始化属性G
        self.G = G


class other(section):
    def __init__(self, A, E, G, I_z, W_t, I_p):
        section.__init__(self, E, G)
        self.A = A
        self.I_z = I_z
        self.W_t = W_t
        self.I_p = I_p


class HC(section):
    """
    初始化圆环截面对象。

    Args:
        De (float): 圆环的外径。
        Di (float): 圆环的内径。
        E (float): 材料的弹性模量。
        G (float): 材料的剪切模量。

    Returns:
        None

    Attributes:
        I_z (float): 圆环截面的惯性矩。
        I_p (float): 圆环截面的极惯性矩。
        W_t (float): 圆环截面的抗扭截面模量。
        De (float): 圆环的外径。
        Di (float): 圆环的内径。
        alpha (float): 圆环内外径之比。
    """

    def __init__(self, De, Di, E, G):
        # 调用父类section的构造函数
        section.__init__(self, E, G)

        # 计算内外径比值
        alpha = Di / De

        # 计算极惯性矩
        self.I_z = pi * De**4 / 64 * (1 - alpha**4)

        # 计算惯性矩
        self.I_p = pi * De**4 / 32 * (1 - alpha**4)

        # 计算抗扭截面模量
        self.W_t = pi * De**3 / 16 * (1 - alpha**4)

        # 保存外径值
        self.De = De

        # 保存内径值
        self.Di = Di

        # 保存内外径比值
        self.alpha = alpha

        self.A = pi * (De**2 - Di**2) / 4


"""
class pole(section):
    def __init__(self, longueur, Maximum_shear_stress, maximum_shear_stress):
"""


class C(section):
    def __init__(self, D, E, G):
        # 调用父类section的构造函数
        section.__init__(self, E, G)

        self.I_z = pi * D**4 / 64
        self.I_p = pi * D**4 / 32
        self.W_t = pi * D**3 / 16
        self.D = D
        self.A = pi * D**2 / 4
