def solve(n, a_list, x):
    s = sum(a_list)
    res = n * (x // s)
    v = s * (x // s)
    for i in range(n):
        v += a_list[i]
        res += 1
        if v > x:
            break
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    x = int(input())
    res = solve(n, a_list, x)
    print(res)


def test():
    assert solve(3, [3, 5, 2], 26) == 8
    assert solve(4, [12, 34, 56, 78], 1000) == 23


if __name__ == "__main__":
    test()
    main()
