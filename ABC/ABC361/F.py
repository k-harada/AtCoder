import math


def solve(n):
    # 3乗以上
    b = 3
    res_set = [1]
    while 2 ** b <= n:
        for i in range(2, n + 1):
            x = i ** b
            if x <= n:
                res_set.append(i ** b)
            else:
                b += 1
                break
    res_list = list(sorted(list(set(res_set))))
    # print(len(res_list))
    m = round(math.sqrt(n))
    if m ** 2 <= n < (m + 1) ** 2:
        res = m + len(res_list)
    else:
        res = m - 1 + len(res_list)
    for r in res_list:
        s = round(math.sqrt(r))
        if s ** 2 == r:
            res -= 1
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(99) == 12
    assert solve(1000000000000000000) == 1001003332


if __name__ == "__main__":
    test()
    main()
