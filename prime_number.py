a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
a = int(a)
b = int(b)


# aの判定
a_answer = "素数です。"
a_count = 2
if a <= 1:
    a_answer = "素数ではありません。"
else:
    while not a_count == a:
        if a % a_count == 0:
            a_answer = "素数ではありません。"
            break
        a_count += 1
print(a_answer)


# bの判定
b_answer = "素数です。"
b_count = 2
if b <= 1:
    b_answer = "素数ではありません。"
else:
    while not b_count == b:
        if b % b_count == 0:
            b_answer = "素数ではありません。"
            break
        b_count += 1
print(b_answer)