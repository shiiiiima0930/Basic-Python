from math import sin, pi
# --example--
# print(sin(0))
# >>> 0
# -----------

a = 0
b = pi / 2
N = 100

S = 0
h = (b - a) / N

f = sin

for k in range(1, N+1):
    x1 = a + (k - 1) * h
    x2 = a + k * h
    S += (f(x1) + f(x2)) * h / 2

print(S)
