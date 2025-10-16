def solve(n, m, a_list):
    s = sum(a_list)
    if m >= s:
        return "Yes"
    else:
        return "No"


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve(5, 15, [3, 1, 4, 1, 5]) == "Yes"
    assert solve(5, 5, [3, 1, 4, 1, 5]) == "No"
    assert solve(1, 10000, [100]) == "Yes"


if __name__ == "__main__":
    test()
    main()
