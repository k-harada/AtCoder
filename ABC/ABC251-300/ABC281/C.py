def solve(n, t, a_list):
    s = sum(a_list)
    r = t % s
    for i, a in enumerate(a_list):
        if r < a:
            return f"{i + 1} {r}"
        else:
            r -= a
    return "0 0"


def main():
    n, t = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, t, a_list)
    print(res)


def test():
    assert solve(3, 600, [180, 240, 120]) == "1 60"
    assert solve(3, 281, [94, 94, 94]) == "3 93"
    assert solve(10, 5678912340, [1000000000] * 10) == "6 678912340"


if __name__ == "__main__":
    test()
    main()
