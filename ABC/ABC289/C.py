def solve(n, m, c_list, a):
    v_list = []
    for i in range(m):
        v = 0
        for k in a[i]:
            v += 2 ** (k - 1)
        v_list.append(v)

    res = 0
    for i in range(2 ** m):
        r = 0
        for j in range(m):
            if (i >> j) & 1:
                r |= v_list[j]
        if r == 2 ** n - 1:
            res += 1
    return res


def main():
    n, m = map(int, input().split())
    c_list = []
    a = []
    for _ in range(m):
        c = int(input())
        a_list = list(map(int, input().split()))
        c_list.append(c)
        a.append(a_list)
    res = solve(n, m, c_list, a)
    print(res)


def test():
    assert solve(3, 3, [2, 2, 1], [[1, 2], [1, 3], [2]]) == 3
    assert solve(4, 2, [2, 2], [[1, 2], [1, 3]]) == 0
    assert solve(6, 6, [3, 3, 2, 3, 3, 2], [[2, 3, 6], [2, 4, 6], [3, 6], [1, 5, 6], [1, 3, 6], [1, 4]]) == 18


if __name__ == "__main__":
    test()
    main()
