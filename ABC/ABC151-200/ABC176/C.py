def solve(n, a_list):
    cum_max = 0
    res = 0
    for i in range(n):
        a = a_list[i]
        if a < cum_max:
            res += cum_max - a
        cum_max = max(a, cum_max)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(5, [2, 1, 5, 4, 3]) == 4
    assert solve(5, [3, 3, 3, 3, 3]) == 0


if __name__ == "__main__":
    test()
    main()
