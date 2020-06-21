def solve(n, k, p_list):
    p_list_s = list(sorted(p_list))
    return sum(p_list_s[:k])


def main():
    n, k = map(int, input().split())
    p_list = list(map(int, input().split()))
    res = solve(n, k, p_list)
    print(res)


def test():
    assert solve(5, 3, [50, 100, 80, 120, 80]) == 210
    assert solve(1, 1, [1000]) == 1000


if __name__ == "__main__":
    test()
    main()
