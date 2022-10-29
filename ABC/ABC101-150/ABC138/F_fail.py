import numpy as np
LARGE = 10 ** 9 + 7


def get_l(vl, le_r):
    # vl <= L <= R <= 2 ** le_r - 1
    res_ = 0

    if vl == 0:
        res_ += pow(2, le_r, LARGE)
        vl = 1
    for l_ in range(le_r):
        if vl % (2 ** (l_ + 1)) != 0:
            le_total = le_r - bin(vl).count("1")
            res_ += pow(3, l_, LARGE) * pow(2, le_total - l_, LARGE)
            res_ %= LARGE
            vl += 2 ** l_
    return res_


def get_r(vr):
    # 0 <= L <= R <= vr
    if vr == 0:
        return 1
    elif vr == 1:
        return 3
    l_ = 0
    while True:
        if 2 ** (l_ + 1) - 1 > vr:
            break
        l_ += 1
    if 2 ** l_ - 1 == vr:
        return pow(3, l_, LARGE)
    else:
        return (pow(3, l_, LARGE) + 2 * get_r(vr - 2 ** l_)) % LARGE


def solve_F(L, R):
    res = 0
    le = 0
    left = 2 ** le
    right = 2 ** (le + 1) - 1

    while True:
        if right < L:
            pass
        elif L <= left <= right <= R:
            res += pow(3, le, LARGE)
        elif R < left:
            break
        elif left <= L <= right < R:
            res += get_l(L, le + 1)
        elif L <= left <= R <= right:
            res += get_r(R - left)
        elif L < R:
            # left <= L <= R <= right:
            # find mid
            mid = left
            for le2 in range(le - 1, -1, -1):
                if L < mid + 2 ** le2 <= R:
                    res += get_l(L - mid, le2)
                    res += get_r(R - mid - 2 ** le2)
                elif mid + 2 ** le2 <= L:
                    mid += 2 ** le2
                else:
                    pass
        else:
            res += 1

        res %= LARGE
        # print(res, left, right)
        le += 1
        left *= 2
        right *= 2
        right += 1
    return res


def solve_greed_f(L, R):

    res_g = 0

    for i in range(L, R + 1):
        for j in range(i, R + 1):
            if j % i == j ^ i:
                res_g += 1

    return res_g


test = True
if __name__ == "__main__":
    if test:
        for L in range(1, 101):
            for R in range(L, 101):
                res = solve_F(L, R)
                res_g = solve_greed_f(L, R)
                if res != res_g:
                    print(L, R, res, res_g)
    else:
        L, R = map(int, input().split())
        print(solve_F(L, R))
