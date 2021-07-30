def solve(n, cp_list, q, lr_list):
    score_a_cum = [0]
    score_b_cum = [0]

    for c, p in cp_list:
        if c == 1:
            score_a_cum.append(score_a_cum[-1] + p)
            score_b_cum.append(score_b_cum[-1])
        else:
            score_a_cum.append(score_a_cum[-1])
            score_b_cum.append(score_b_cum[-1] + p)

    res = []
    for l, r in lr_list:
        res_a = score_a_cum[r] - score_a_cum[l - 1]
        res_b = score_b_cum[r] - score_b_cum[l - 1]
        res.append(f'{res_a} {res_b}')
    # print(res)
    return res


def main():
    n = int(input())
    cp_list = [tuple(map(int, input().split())) for _ in range(n)]
    q = int(input())
    lr_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, cp_list, q, lr_list)
    for r in res:
        print(r)


def test():
    assert solve(7, [(1, 72), (2, 78), (2, 94), (1, 23), (2, 89), (1, 40), (1, 75)], 1, [(2, 6)]) == ["63 261"]


if __name__ == "__main__":
    test()
    main()
