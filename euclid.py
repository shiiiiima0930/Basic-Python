a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a = int(a)
b = int(b)
while b != 0:
    a, b = b, a % b
print(a)
