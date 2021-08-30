def solve(n, m, a_list, b_list, c_list):
    bcr_list = [(b, c, c / b) for b, c in zip(b_list, c_list)]
    bcr_list_s = list(sorted(bcr_list, key=lambda x: -x[2]))
    print(bcr_list_s)

    return 0


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    res = solve(n, m, a_list, b_list, c_list)
    print(res)


def test():
    assert solve(3, 3, [2, 5, 5], [1, 2, 2], [5, 3, 5]) == 0  # 11
    assert solve(10, 6, [3, 54, 62, 64, 25, 89, 1, 47, 77, 4], [1, 17, 10, 29, 95, 17], [32, 40, 90, 27, 50, 9]) == 0  # 211


if __name__ == "__main__":
    test()
    main()
