LARGE = 1000000007


def solve(n, a_list):

    x = -1
    y = -1
    z = -1
    res = 1

    for i in range(n):
        c = 0
        a = a_list[i]
        if x == a - 1:
            c += 1
        if y == a - 1:
            c += 1
        if z == a - 1:
            c += 1
        if x == a - 1:
            x += 1
        elif y == a - 1:
            y += 1
        else:
            z += 1
        res *= c
        res %= LARGE
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(6, [0, 1, 2, 3, 4, 5]) == 3
    assert solve(3, [0, 0, 0]) == 6


if __name__ == "__main__":
    test()
    main()
