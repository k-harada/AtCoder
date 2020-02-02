def solve(n, k):
    s1 = n * (k + (k + 2 * n - 1))
    s2 = n * ((k + 2 * n) + (k + 3 * n - 1)) // 2
    res = []
    if s1 > s2:
        return None
    if n % 2 == 1:
        m = ((n + 1) // 4) * 2
        for i in range(m):
            a = k + n - 1 - i
            b = k + n + i + (m - 1 - 2 * i)
            c = k + 2 * n + (n - 1) // 2 + (m - 1 - 2 * i)
            res.append([a, b, c])
            # print(1, a, b, c)
        for i in range(n - m):
            a = k + n - 1 - m - i
            b = k + 2 * n - 1 - i
            c = k + 2 * n + (n - 1) // 2 + 2 * ((n - m) // 2 - i)
            res.append([a, b, c])
            # print(2, a, b, c)
        return res
    else:
        m = n // 2
        for i in range(m):
            a = k + n - 1 - i
            b = k + n + i + (m - 1 - 2 * i)
            c = k + 2 * n + m + (m - 2 - 2 * i)
            res.append([a, b, c])
            # print(1, a, b, c)
        for i in range(n - m):
            a = k + n - 1 - m - i
            b = k + 2 * n - 1 - i
            c = k + 3 * n - 1 - 2 * i
            res.append([a, b, c])
            # print(2, a, b, c)
        return res


def main():
    n, k = map(int, input().split())
    res = solve(n, k)
    if res is None:
        print(-1)
    else:
        for r in res:
            print(*r)


if __name__ == "__main__":
    main()
