def solve(n, a_list, b_list):
    res = 0
    for a, b in zip(sorted(a_list), sorted(b_list)):
        res += abs(a - b)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    print(res)


def test():
    assert solve(1, [869], [120]) == 749
    assert solve(6, [8, 6, 9, 1, 2, 0], [1, 5, 7, 2, 3, 9]) == 5


if __name__ == "__main__":
    test()
    main()
