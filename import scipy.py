from scipy import integrate


def f(x):
    return x + 1


result, error = integrate.quad(f, 1, 2)
print(result)
