def solve(n, a_list):
    return sum(a_list)


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [2, 7, 2]) == 11
    assert solve(1, [3]) == 3


if __name__ == "__main__":
    test()
    main()
