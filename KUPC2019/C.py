def solve_c(m, k):
    res = 0
    max_m = 0
    while max_m < m:
        res += 1
        max_m = (2 * max_m + 1) * k + max_m
    return res


def main():
    m, k = map(int, input().split())
    res = solve_c(m, k)
    print(res)


def test():
    assert solve_c(5, 1) == 3
    assert solve_c(8, 2) == 2


if __name__ == "__main__":
    test()
    main()
