from itertools import product


def solve(n, a_array):

    res = -100000000

    for p in product([0, 1, 2], repeat=n):
        res_temp = 0
        for i in range(n):
            for j in range(n):
                if p[i] == p[j]:
                    res_temp += a_array[i][j]
        res = max(res, res_temp)

    return res


def main():
    n = int(input())
    a_array = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        a_list = list(map(int, input().split()))
        for j in range(i + 1, n):
            a_array[i][j] = a_list[j - i - 1]
    res = solve(n, a_array)
    print(res)


def test():
    assert solve(6, [
        [0, 10, 10, -10, -10, -10],
        [0, 0, 10, -10, -10, -10],
        [0, 0, 0, -10, -10, -10],
        [0, 0, 0, 0, 10, -10],
        [0, 0, 0, 0, 0, -10],
        [0, 0, 0, 0, 0, 0]
    ]) == 40
    assert solve(3, [[0, 1, 1], [0, 0, 1], [0, 0, 0]]) == 3


if __name__ == "__main__":
    test()
    main()
