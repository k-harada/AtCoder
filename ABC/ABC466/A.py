def solve(n, a_list):
    if max(a_list) < 0:
        res = "Yes"
    else:
        res = "No"
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(4, [2, 0, -1, 2]) == "No"
    assert solve(3, [-5, -2, -1]) == "Yes"
    assert solve(4, [0, -2, 0, -1]) == "No"


if __name__ == "__main__":
    test()
    main()
