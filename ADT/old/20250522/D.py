def solve(n, a_list):
    a_list_s = list(sorted(a_list))
    r = a_list_s[-2]
    for i, a in enumerate(a_list):
        if a == r:
            return i + 1
    return -1


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(6, [1, 123, 12345, 12, 1234, 123456]) == 3
    assert solve(5, [3, 1, 4, 15, 9]) == 5


if __name__ == "__main__":
    test()
    main()
