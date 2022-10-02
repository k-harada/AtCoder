def solve(n):
    if n == 3:
        return [[3, 5, 4], [9, 7, 2], [1, 8, 6]]
    elif n == 4:
        return [[15, 11, 16, 12], [13, 3, 6, 9], [14, 7, 8, 1], [4, 2, 10, 5]]
    elif n == 5:
        return [[1, 7, 13, 19, 23], [5, 11, 17, 21, 25], [3, 9, 15, 24, 20], [6, 12, 18, 2, 8], [14, 22, 4, 10, 16]]
    res = [[0] * n for _ in range(n)]
    i = 0
    j = 0
    for k in range(1, n * n + 1, 6):
        res[i][j] = k
        j += 1
        if j == n:
            j = 0
            i += 1
    for k in range(5, n * n + 1, 6):
        res[i][j] = k
        j += 1
        if j == n:
            j = 0
            i += 1
    for k in range(3, n * n + 1, 6):
        res[i][j] = k
        j += 1
        if j == n:
            j = 0
            i += 1
    for k in range(6, n * n + 1, 6):
        res[i][j] = k
        j += 1
        if j == n:
            j = 0
            i += 1
    for k in range(4, n * n + 1, 6):
        res[i][j] = k
        j += 1
        if j == n:
            j = 0
            i += 1
    for k in range(2, n * n + 1, 6):
        res[i][j] = k
        j += 1
        if j == n:
            j = 0
            i += 1
    # print(res)
    return res


def main():
    n = int(input())
    res = solve(n)
    for r in res:
        print(" ".join([str(b) for b in r]))


def test():
    assert solve(4) == [[15, 11, 16, 12], [13, 3, 6, 9], [14, 7, 8, 1], [4, 2, 10, 5]]


if __name__ == "__main__":
    test()
    main()
