def solve(n, a_list):
    d = dict()
    for a in a_list:
        d[a] = -1
    res = [0] * n
    for i, a in enumerate(a_list):
        res[i] = d[a]
        d[a] = i + 1
    return " ".join([str(r) for r in res])


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(5, [1, 2, 1, 1, 3]) == "-1 -1 1 3 -1"
    assert solve(4, [1, 1000000000, 1000000000, 1]) == "-1 -1 2 1"


if __name__ == "__main__":
    test()
    main()
