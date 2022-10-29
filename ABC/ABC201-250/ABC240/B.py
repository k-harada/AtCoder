def solve(n, a_list):
    return len(set(a_list))


def main():
    n = int(input())
    a_list = map(int, input().split())
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(6, [1, 4, 1, 2, 2, 1]) == 3
    assert solve(1, [1]) == 1
    assert solve(11, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 7


if __name__ == "__main__":
    test()
    main()
