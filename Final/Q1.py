"""
Question 1: Controlled Prime Numbers
@author: Aryan Ahadinia
"""

def is_in_new_list(sorted_list: list, value_index) -> list:
    for i in range(value_index):
        if sorted_list[value_index] % sorted_list[i] == 0:
            return False
    return True


def remove_multiple(L: list) -> list:
    new_list = []
    L.sort()
    for i in range(len(L)):
        if is_in_new_list(L, i):
            new_list.append(L[i])
    return new_list


def is_devidable_by_list(L: list, value: int) -> bool:
    for d in L:
        if value % d == 0:
            return True
    return False


def controlled_primes(Lp: list, m: int, n: int) -> list:
    Lp = remove_multiple(Lp)
    l = []
    for i in range(m + 1, n):
        if not is_devidable_by_list(Lp, i):
            l.append(i)
    return l
