def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def solve(n, x, y, pt_list, q, q_list):
    LCM = 1
    for p, t in pt_list:
        LCM = lcm(LCM, p)
    res_add = [-1] * LCM
    res_list = []
    for s in q_list:
        if res_add[s % LCM] >= 0:
            res_list.append(s + res_add[s % LCM])
        else:
            s_ = s + x
            for p, t in pt_list:
                s_ += (- s_ % p) + t
            s_ += y
            res_add[s % LCM] = s_ - s
            res_list.append(s_)

    return res_list


def main():
    n, x, y = map(int, input().split())
    pt_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    q = int(input())
    q_list = [int(input()) for _ in range(q)]
    res = solve(n, x, y, pt_list, q, q_list)
    for r in res:
        print(r)


def test():
    assert solve(4, 2, 3, [
        (5, 4), (6, 6), (3, 1)
    ], 7, [
        13, 0, 710511029, 136397527, 763027379, 644706927, 447672230
    ]) == [34, 22, 710511052, 136397548, 763027402, 644706946, 447672250]


if __name__ == "__main__":
    test()
    main()
