def solve(n, a_list):
    if len(set(a_list)) == n:
        return "YES"
    else:
        return "NO"


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(5, [2, 6, 1, 4, 5]) == "YES"
    assert solve(6, [4, 1, 3, 1, 6, 2]) == "NO"
    assert solve(2, [10000000, 10000000]) == "NO"


if __name__ == "__main__":
    test()
    main()
