import matplotlib.pyplot as plt


# 定义函数
def f(x):
    return x**2


# 生成数据点
x_values = range(-10, 11)
y_values = [f(x) for x in x_values]

# 绘制函数图
plt.plot(x_values, y_values)

# 添加标题和标签
plt.title("Function Plot of f(x) = x^2")
plt.xlabel("x axis")
plt.ylabel("y axis")

# 显示图形
plt.show()
