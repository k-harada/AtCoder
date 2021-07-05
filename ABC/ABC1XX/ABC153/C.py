def solve(n, k, h_list):
    h_list_s = list(sorted(h_list))
    if k >= n:
        return 0
    elif k > 0:
        return sum(h_list_s[:-k])
    else:
        return sum(h_list_s)


def main():
    n, k = map(int, input().split())
    h_list = list(map(int, input().split()))
    res = solve(n, k, h_list)
    print(res)


def test():
    assert solve(3, 1, [4, 1, 5]) == 5
    assert solve(8, 9, [7, 9, 3, 2, 8, 4, 6]) == 0
    assert solve(3, 0, [1000000000, 1000000000, 1000000000]) == 3000000000


if __name__ == "__main__":
    test()
    main()