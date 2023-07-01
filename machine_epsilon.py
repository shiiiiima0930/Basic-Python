# TODO
epsilon = 1
small = 1
while True:
    small *= 1/2
    if 1 + epsilon > 1:
        epsilon = small
    else:
        break

print(epsilon)