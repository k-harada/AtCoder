def solve(n, m):
    res_list = []
    if n % 2 == 1:
        for i in range(m):
            res_list.append([i + 1, 2 * m - i])
    else:
        k = (m + 1) // 2
        for i in range(k):
            res_list.append([i + 1, 2 * k - i])
        for i in range(m - k):
            res_list.append([2 * k + i + 1, 2 * m + 1 - i])
    return res_list


def main():
    n, m = map(int, input().split())
    res = solve(n, m)
    for r in res:
        print(" ".join([str(a) for a in r]))


def eval_res(n, ab_list):
    eval_dict = dict()
    for a, b in ab_list:
        d = (a - b) % n
        if d in eval_dict.keys():
            return False
        eval_dict[d] = 1
        d = (b - a) % n
        if d in eval_dict.keys():
            return False
        eval_dict[d] = 1
    return True


def test():
    assert eval_res(4, solve(4, 1))
    assert eval_res(7, solve(7, 3))


if __name__ == "__main__":
    test()
    main()
