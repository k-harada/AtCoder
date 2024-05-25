def solve(n, m, a_list):
    res_bit = [0] * n
    for j in range(m):
        v_bit = [0] * 1000
        for i in range(n):
            res_bit[i] ^= v_bit[a_list[i][j]]
            v_bit[a_list[i][j]] += 2 ** i
    # print(res_bit)
    res = 0
    for i in range(n):
        res += bin(res_bit[i]).count("1")
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    a_list = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(3, 3, [[1, 2, 3], [1, 3, 4], [2, 3, 4]]) == 1
    assert solve(6, 5, [
        [8, 27, 27, 10, 24],
        [27, 8, 2, 4, 5],
        [15, 27, 26, 17, 24],
        [27, 27, 27, 27, 27],
        [27, 7, 22, 11, 27],
        [19, 27, 27, 27, 27]
    ]) == 5


if __name__ == "__main__":
    test()
    main()
