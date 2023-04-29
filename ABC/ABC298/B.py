def rot90(n, x):
    y = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            y[i][j] = x[n - 1 - j][i]
    return y


def equal(n, x, y):
    for i in range(n):
        for j in range(n):
            if x[i][j] == 1 and y[i][j] == 0:
                return False
    return True


def solve(n, a, b):
    if equal(n, a, b):
        return "Yes"
    a1 = rot90(n, a)
    if equal(n, a1, b):
        return "Yes"
    a2 = rot90(n, a1)
    if equal(n, a2, b):
        return "Yes"
    a3 = rot90(n, a2)
    if equal(n, a3, b):
        return "Yes"
    return "No"


def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, a, b)
    print(res)


def test():
    assert solve(3, [[0, 1, 1], [1, 0, 0], [0, 1, 0]], [[1, 1, 0], [0, 0, 1], [1, 1, 1]]) == "Yes"
    assert solve(2, [[0, 0], [0, 0]], [[1, 1], [1, 1]]) == "Yes"


if __name__ == "__main__":
    test()
    main()
