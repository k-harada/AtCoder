def solve_a(n, x, a_list):
    a_max = max(a_list)
    res = 0
    for i in range(n):
        if a_list[i] + x >= a_max:
            res += 1
    return res


def test():
    assert solve_a(5, 5, [1, 3, 5, 7, 9]) == 3
    assert solve_a(5, 2, [1, 3, 5, 7, 9]) == 2


def main():
    n, x = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve_a(n, x, a_list)
    print(res)


if __name__ == "__main__":
    test()
    main()
