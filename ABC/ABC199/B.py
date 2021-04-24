def solve(n, a_list, b_list):
    a_max = max(a_list)
    b_min = min(b_list)
    if a_max > b_min:
        return 0
    else:
        return b_min - a_max + 1


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    print(res)


def test():
    assert solve(2, [3, 2], [7, 5]) == 3
    assert solve(3, [1, 5, 3], [10, 7, 3]) == 0
    assert solve(3, [3, 2, 5], [6, 9, 8]) == 2


if __name__ == "__main__":
    test()
    main()
