from math import sqrt


def isprime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def generate(n):
    if n == 1:
        return [2, 3, 5, 7]
    l = generate(n-1)
    l_n = []
    for i in l:
        for j in (1, 3, 7, 9):
            t = 10*i + j
            if isprime(t):
                l_n.append(t)
    return l_n


n = int(input())
ln = generate(n)
for i in ln:
    print(i)
