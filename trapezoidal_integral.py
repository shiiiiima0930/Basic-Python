from math import sin, pi
# --example--
# print(sin(0))
# >>> 0
# -----------

def f(x):
    return x**2

def trapezoidal_integral(f, a=0, b=1, n=100):
    width = (b-a) / n
    integral = 0
    for i in range(n):
        s = a + width * i
        t = s + width 
        integral += (f(s) + f(t)) * width / 2 
    return integral

a = float(input("左端："))
b = float(input("右端："))
n = int(input("分割数："))
print(trapezoidal_integral(f, a, b, n))
