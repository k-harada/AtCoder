def solve(n, m, a_list, b_list, r1, r2, r3):

    score_list = [[0] * 3 for _ in range(n)]
    penalty_list = [[0] * 3 for _ in range(n)]
    for i in range(n):
        score_list[i][0] = (a_list[i] * b_list[i]) % r1
        score_list[i][1] = (a_list[i] * (b_list[i]) ** 2) % r2
        score_list[i][2] = (a_list[i] * (b_list[i]) ** 3) % r3
        penalty_list[i][0] = a_list[i] * b_list[i]
        penalty_list[i][1] = a_list[i] * (b_list[i]) ** 2
        penalty_list[i][2] = a_list[i] * (b_list[i]) ** 3

    # greedy from round 3


    return 0


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    r1, r2, r3 = map(int, input().split())
    res = solve(n, m, a_list, b_list, r1, r2, r3)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve() == 0
    assert solve() == 0
    assert solve() == 0


if __name__ == "__main__":
    test()
    main()
