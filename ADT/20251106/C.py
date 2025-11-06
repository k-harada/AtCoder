def solve(n, a_list):
    s = sum(a_list)
    a = s // 2
    b = s - max(a_list)
    return min(a, b)


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(4, [1, 2, 3, 3]) == 4
    assert solve(3, [1, 1, 100]) == 2


if __name__ == "__main__":
    test()
    main()
