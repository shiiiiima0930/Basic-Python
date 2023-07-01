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

for k in range(N):
    x1 = a + (k - 1) * h
    x2 = a + k * h
    S += (sin(x1) + sin(x2)) * h / 2

print(S)
