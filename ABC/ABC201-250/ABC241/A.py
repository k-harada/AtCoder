def solve(a_list):
    r = a_list[0]
    r = a_list[r]
    res = a_list[r]
    return res


def main():
    a_list = list(map(int, input().split()))
    res = solve(a_list)
    print(res)


def test():
    assert solve([9, 0, 1, 2, 3, 4, 5, 6, 7, 8]) == 7
    assert solve([4, 8, 8, 8, 0, 8, 8, 8, 8, 8]) == 4
    assert solve([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0


if __name__ == "__main__":
    test()
    main()
