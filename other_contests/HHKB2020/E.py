MOD = 10 ** 9 + 7


def solve(h, w, s_list):

    count = [[1] * w for _ in range(h)]

    for i in range(h):
        left = 0
        for j in range(w):
            if s_list[i][j] == ".":
                count[i][j] += left
                left += 1
            else:
                left = 0

    for i in range(h):
        right = 0
        for j in range(w - 1, -1, -1):
            if s_list[i][j] == ".":
                count[i][j] += right
                right += 1
            else:
                right = 0
    for j in range(w):
        up = 0
        for i in range(h):
            if s_list[i][j] == ".":
                count[i][j] += up
                up += 1
            else:
                up = 0
    for j in range(w):
        down = 0
        for i in range(h - 1, -1, -1):
            if s_list[i][j] == ".":
                count[i][j] += down
                down += 1
            else:
                down = 0

    k = 0
    for i in range(h):
        for j in range(w):
            if s_list[i][j] == ".":
                k += 1
            else:
                count[i][j] = 0

    pow_2 = [1] * (h * w + 1)
    for i in range(1, h * w + 1):
        pow_2[i] = pow_2[i - 1] * 2 % MOD

    res = 0
    for i in range(h):
        for j in range(w):
            res += pow_2[k] - pow_2[k - count[i][j]]
    # print(count)
    # print(res)
    return res % MOD


def main():
    h, w = map(int, input().split())
    s_list = [list(input()) for _ in range(h)]
    res = solve(h, w, s_list)
    print(res)


def test():
    assert solve(1, 5, [[".", ".", "#", ".", "."]]) == 48
    assert solve(2, 3, [[".", ".", "#"], ["#", ".", "."]]) == 52
    # assert solve(2000, 2000, [["."] * 2000 for _ in range(2000)]) == 248765091


if __name__ == "__main__":
    test()
    main()
