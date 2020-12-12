def is_prime(a: int) -> bool:
    if a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


def is_very_prime(a: int) -> bool:
    if 0 < a and a < 10:
        return a in (2, 3, 5, 7)
    return is_prime(a) and is_very_prime(a // 10)


n = int(input())
for i in range(10 ** (n - 1), 10 ** n):
    if is_very_prime(i):
        print(i)


# instead of line 12 we can use:
# if n in (2, 3, 5, 7):
#       return True
# return False