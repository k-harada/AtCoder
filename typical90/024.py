def solve(n, k, a_list, b_list):
    res = sum([abs(a - b) for a, b in zip(a_list, b_list)])
    if res <= k and (k - res) % 2 == 0:
        return "Yes"
    else:
        return "No"


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, k, a_list, b_list)
    print(res)


def test():
    assert solve(2, 5, [1, 3], [2, 1]) == "Yes"
    assert solve(3, 1, [7, 8, 9], [7, 8, 9]) == "No"
    assert solve(7, 999999999, [3, 1, 4, 1, 5, 9, 2], [1, 2, 3, 4, 5, 6, 7]) == "Yes"


if __name__ == "__main__":
    test()
    main()
