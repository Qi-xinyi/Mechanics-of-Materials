from math import *
import pandas as pd


class section:
    """
    初始化函数，用于创建截面对象。

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
    def __init__(self, A, E, G):
        section.__init__(self, E, G)
        self.A = A


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
        self.y_max = De / 2  # 圆环截面的最大y坐标值self
        # 保存内径值
        self.Di = Di
        self.W_z = self.I_z / self.y_max
        # 保存内外径比值
        self.alpha = alpha
        self.A = pi * (De**2 - Di**2) / 4
        self.S_z = De**2 / 2 - Di**2 / 2

        def b1(self, y):
            return (
                ((self.De / 2) ** 2 - y**2) ** 0.5 - (self.Di / 2**2 - y**2) ** 0.5
            ) * 2

        def S_z(self, y):
            if y == 0:
                return pi * (self.De**3 - self.Di**3) / 4
            else:
                S_z = float(input("请输入S_z的值"))
                return S_z


"""
class pole(section):
    def __init__(self, longueur, Maximum_shear_stress, maximum_shear_stress):
"""


class H(section):
    def __init__(self, num1, E, G):
        section.__init__(self, E, G)

        try:
            CSV_PATH = "D:\\材料力学\\程序\\H型钢.csv"
            df = pd.read_csv(CSV_PATH)
            matching_rows = df[df["型号"] == num1]

            if matching_rows.empty:
                raise ValueError(f"未找到型号为 {num1} 的H型钢数据")

            row = matching_rows.iloc[0]

            # 单位转换常量
            LENGTH_TO_M = 1e-3
            AREA_TO_M2 = 1e-4
            MOMENT_TO_M4 = 1e-8
            SECTION_MODULUS_TO_M3 = 1e-6

            self.I_z = float(row["I_z"]) * MOMENT_TO_M4
            self.I_y = float(row["I_y"]) * MOMENT_TO_M4
            self.W_z = float(row["W_z"]) * SECTION_MODULUS_TO_M3
            self.W_y = float(row["W_y"]) * SECTION_MODULUS_TO_M3
            self.A = float(row["A"]) * AREA_TO_M2
            self.y_max = float(row["h"]) / 2 * LENGTH_TO_M
            h = 2 * self.y_max
            self.t = float(row["t"]) * LENGTH_TO_M
            self.h_0 = h - 2 * self.t
            self.b = float(row["b"]) * LENGTH_TO_M
            self.b_0 = float(row["d"]) * LENGTH_TO_M

        except FileNotFoundError:
            raise FileNotFoundError(f"无法找到H型钢数据文件: {CSV_PATH}")
        except KeyError as e:
            raise KeyError(f"CSV文件中缺少必要的列: {e}")

    def S_(self, y):
        a = self.b / 8 * (self.h**2 - self.h_0**2) + self.b_0 / 2 * (
            self.h_0**2 / 4 - y**2
        )
        return a

    def b(self, y):
        if abs(y) <= self.h / 2:
            return self.b_0
        else:
            return self.b


class C(section):
    def __init__(self, D, E, G):
        # 调用父类section的构造函数
        section.__init__(self, E, G)
        self.I_z = pi * D**4 / 64
        self.I_p = pi * D**4 / 32
        self.W_t = pi * D**3 / 16
        self.D = D
        self.A = pi * D**2 / 4
        self.y_max = D / 2
        self.W_z = pi * self.D**3 / 32

        def S_z(self, y):
            return (
                (self.D**2 / 8 - y) * (-pi + 2 * asin(y / (self.D / 2)))
                - y**2 * (y / ((self.D / 2) ** 2 - y**2) ** 0.5)
                + (self.D**2 / 4 - y**2) * (self.D / 2**2 - y**2) ** 0.5
            )

        # def S_z(self, y):
        #     # 计算截面面积的函数
        #     if y == 0:
        #         return pi * self.D**3 / 4 / 3 * pi
        #     else:
        #         print("y不为0，不会")

        def b1(self, y):
            return (((self.D / 2) ** 2 - y**2) ** 0.5) * 2


class Q(section):
    def __init__(self, b, h, E, G):
        section.__init__(self, E, G)
        self.b = b
        self.h = h
        self.A = b * h
        self.I_z = b * h**3 / 12
        self.y_max = h / 2
        self.W_z = self.I_z / self.y_max

    def S_z(self, y):
        return self.b / 2 * (self.h**2 - y**2)

    def b1(self, y):
        return self.b


class TC(section):  # Thin-walled cylinders
    def __init__(self, D, t, E, G):
        # 调用父类section的构造函数,
        section.__init__(self, E, G)
        self.I_p = 2 * pi * D**3 * t / 8
