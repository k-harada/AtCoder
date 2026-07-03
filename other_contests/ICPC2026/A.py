def solve(n, a_list):
    if 2 in a_list:
        res = 2
    elif 1 in a_list:
        res = 1
    else:
        res = max(a_list)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(4, [2, 1, 10, 12]) == 2
    assert solve(7, [3, 4, 5, 4, 3, 4, 5]) == 5
    assert solve(6, [3, 11, 13, 7, 8, 3]) == 13


if __name__ == "__main__":
    test()
    main()
