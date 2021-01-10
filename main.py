from math import ceil, log10
from random import randint
def generate():
    total = [42, 139, 236, 333][randint(0, 3)]
    l = randint(max(0, ceil((total - 9 * sum(list(range(9)))) / 10)), min(total // 10, 9)) * 10
    total -= l
    for i in range(2, 9):
        new = randint(max(0, ceil((total - 9 * sum(list(range(10 - i)))) / (10 - i))), min(total // (10 - i), 9))
        l += new * 10 ** (10 - i)
        total -= new * (10 - i)
    return l + total
def check(x):
    l = [0] * (9 - ceil(log10(x + 1))) + list(map(int, list(str(x))))
    return l[0] * 8 + l[1] * 7 + l[2] * 6 + l[3] * 5 + l[4] * 4 + l[5] * 3 + l[6] * 2 + l[7] * 10 + l[8] in [42, 139, 236, 333]
