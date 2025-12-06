def solve(n, a_list):
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            s = sum(a_list[i:j + 1])
            r = 1
            for k in range(i, j + 1):
                if s % a_list[k] == 0:
                    r = 0
            res += r
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(5, [8, 6, 10, 5, 7]) == 6
    assert solve(3, [1, 1, 1]) == 0


if __name__ == "__main__":
    test()
    main()
