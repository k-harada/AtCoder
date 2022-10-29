def solve(n, p, a_list):
    res = sum([1 for i in range(n) if a_list[i] < p])
    return res


def main():
    n, p = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, p, a_list)
    print(res)


def test():
    assert solve(4, 50, [80, 60, 40, 0]) == 2
    assert solve(3, 90, [89, 89, 89]) == 3
    assert solve(2, 22, [6, 37]) == 1


if __name__ == "__main__":
    test()
    main()
