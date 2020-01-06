def solve(abc6):
    abc6_s = list(sorted(abc6))
    return abc6_s[3]


def main():
    abc6 = list(map(int, input().split()))
    res = solve(abc6)
    print(res)


def test():
    assert solve([4, 18, 25, 20, 9, 13]) == 18
    assert solve([95, 96, 97, 98, 99, 100]) == 98
    assert solve([19, 92, 3, 35, 78, 1]) == 35


if __name__ == "__main__":
    test()
    main()
