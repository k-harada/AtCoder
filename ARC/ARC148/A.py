def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solve(n, a_list):

    a_min = min(a_list)
    a_max = max(a_list)
    d = a_max - a_min

    if d == 0:
        return 1
    for i in range(n):
        d = gcd(d, a_list[i] - a_min)
    if d >= 2:
        return 1

    return 2


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [1, 4, 8]) == 2
    assert solve(4, [5, 10, 15, 20]) == 1
    assert solve(10, [3785, 5176, 10740, 7744, 3999, 3143, 9028, 2822, 4748, 6888]) == 1


if __name__ == "__main__":
    test()
    main()
