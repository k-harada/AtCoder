def solve(n, a_list):
    called = [0] * (n + 1)
    called[0] = 1
    for i, a in enumerate(a_list):
        if called[i + 1] == 0:
            called[a] = 1
    res = []
    res.append(str(n + 1 - sum(called)))
    res.append(" ".join([str(i) for i in range(n + 1) if called[i] == 0]))
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [3, 1, 4, 5, 4]) == ["2", "2 4"]
    assert solve(20, [9, 7, 19, 7, 10, 4, 13, 9, 4, 8, 10, 15, 16, 3, 18, 19, 12, 13, 2, 12]) == [
        "10", "1 2 5 6 8 11 14 17 18 20"
    ]


if __name__ == "__main__":
    test()
    main()
