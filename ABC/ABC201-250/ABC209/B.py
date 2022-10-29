def solve(n, x, a_list):
    cost = sum(a_list) - n // 2
    if x >= cost:
        return "Yes"
    else:
        return "No"


def main():
    n, x = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, x, a_list)
    print(res)


def test():
    assert solve(2, 3, [1, 3]) == "Yes"
    assert solve(4, 10, [3, 3, 4, 4]) == "No"
    assert solve(8, 30, [3, 1, 4, 1, 5, 9, 2, 6]) == "Yes"


if __name__ == "__main__":
    test()
    main()
