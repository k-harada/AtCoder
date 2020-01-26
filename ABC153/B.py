def solve(h, n, a_list):
    if sum(a_list) >= h:
        return "Yes"
    else:
        return "No"


def main():
    h, n = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(h, n, a_list)
    print(res)


def test():
    assert solve(10, 3, [4, 5, 6]) == "Yes"
    assert solve(20, 3, [4, 5, 6]) == "No"
    assert solve(210, 5, [31, 41, 59, 26, 53]) == "Yes"
    assert solve(211, 5, [31, 41, 59, 26, 53]) == "No"


if __name__ == "__main__":
    test()
    main()
