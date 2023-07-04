a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO

#問３
a = int(a)
b = int(b)

def euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(euclid(a, b))

#問４
def relatively_prime(a, b):
    while b != 0:
        a, b = b, a % b
        if a == 1:
            return "互いに素"
    return "互いに素ではない"

print(relatively_prime(a, b))

