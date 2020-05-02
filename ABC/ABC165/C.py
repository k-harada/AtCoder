from itertools import combinations


def solve(n, m, q, q_list):

    res_max = 0

    # 0-1
    a_list = [0] * n
    for com in combinations(range(n + m - 1), n):

        for i, c in enumerate(com):
            if i == 0:
                a_list[i] = c + 1
            else:
                a_list[i] = a_list[i - 1] + c - com[i - 1] - 1
        # print(a_list)
        res = 0
        for i in range(q):
            a, b, c, d = q_list[i]
            if a_list[b - 1] - a_list[a - 1] == c:
                res += d

        if res > res_max:
            res_max = res
    # print(res_max)
    return res_max


def main():
    n, m, q = map(int, input().split())
    q_list = [list(map(int, input().split())) for _ in range(q)]
    res = solve(n, m, q, q_list)
    print(res)


def test():
    assert solve(3, 4, 3, [[1, 3, 3, 100], [1, 2, 2, 10], [2, 3, 2, 10]]) == 110
    assert solve(4, 6, 10, [
        [2, 4, 1, 86568], [1, 4, 0, 90629], [2, 3, 0, 90310], [3, 4, 1, 29211], [3, 4, 3, 78537],
        [3, 4, 2, 8580], [1, 2, 1, 96263], [1, 4, 2, 2156], [1, 2, 0, 94325], [1, 4, 3, 94328]
    ]) == 357500
    assert solve(10, 10, 1, [[1, 10, 9, 1]]) == 1


if __name__ == "__main__":
    test()
    main()
