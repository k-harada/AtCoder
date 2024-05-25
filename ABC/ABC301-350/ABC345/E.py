def solve(n, k, cv_list):

    dp1 = [[-1] * (k + 1) for _ in range(2)]
    dp2 = [[-1] * (k + 1) for _ in range(2)]
    dpc = [[-1] * (k + 1) for _ in range(2)]
    dp1[0][0] = 0
    dp2[0][0] = 0
    dpc[0][0] = 0
    for i in range(n):
        c, v = cv_list[i]
        for j in range(k + 1):
            if j < k:
                # i番目を残さない
                dp1[(i + 1) % 2][j + 1] = dp1[i % 2][j]
                dp2[(i + 1) % 2][j + 1] = dp2[i % 2][j]
                dpc[(i + 1) % 2][j + 1] = dpc[i % 2][j]
        dp1[(i + 1) % 2][0] = -1
        dp2[(i + 1) % 2][0] = -1
        dpc[(i + 1) % 2][0] = -1

        for j in range(k + 1):
            # i番目を残す
            if dpc[i % 2][j] == c:
                if dp2[i % 2][j] >= 0:
                    x = dp2[i % 2][j] + v
                else:
                    x = -10
            else:
                if dp1[i % 2][j] >= 0:
                    x = dp1[i % 2][j] + v
                else:
                    x = -10
            if x >= dp1[(i + 1) % 2][j]:
                if dpc[(i + 1) % 2][j] == c:
                    dp1[(i + 1) % 2][j] = x
                else:
                    dp2[(i + 1) % 2][j] = dp1[(i + 1) % 2][j]
                    dp1[(i + 1) % 2][j] = x
                    dpc[(i + 1) % 2][j] = c
            elif x >= dp2[(i + 1) % 2][j]:
                if dpc[(i + 1) % 2][j] == c:
                    pass
                else:
                    dp2[(i + 1) % 2][j] = x
        # print(dp1)
    return dp1[n % 2][k]


def main():
    n, k = map(int, input().split())
    cv_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, k, cv_list)
    print(res)


def test():
    assert solve(5, 2, [(1, 1), (3, 5), (3, 3), (1, 4), (1, 2)]) == 10
    assert solve(3, 1, [(1, 10), (1, 10), (1, 10)]) == -1
    assert solve(3, 1, [(1, 1), (2, 2), (3, 3)]) == 5


def test_large():
    print(solve(200000, 500, [(i + 1, i + 1) for i in range(200000)]))


if __name__ == "__main__":
    test()
    # test_large()
    main()
