# TODO
def prime_number(n):
    if not isinstance(n, int) or n < 0:
        raise TypeError
    elif n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

print(prime_number(61))
print(prime_number(10))