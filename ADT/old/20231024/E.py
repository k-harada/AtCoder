def solve(n, m, b):
    for i in range(n - 1):
        for j in range(m):
            if b[i + 1][j] != b[i][j] + 7:
                return "No"
    for i in range(n):
        for j in range(m - 1):
            if b[i][j + 1] != b[i][j] + 1:
                return "No"
    for j in range(m - 1):
        if (b[0][j + 1] - 1) % 7 != (b[0][j] - 1) % 7 + 1:
            return "No"
    return "Yes"


def main():
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, m, b)
    print(res)


def test():
    assert solve(2, 3, [[1, 2, 3], [8, 9, 10]]) == "Yes"
    assert solve(2, 1, [[1], [2]]) == "No"
    assert solve(10, 4, [
        [1346, 1347, 1348, 1349],
        [1353, 1354, 1355, 1356],
        [1360, 1361, 1362, 1363],
        [1367, 1368, 1369, 1370],
        [1374, 1375, 1376, 1377],
        [1381, 1382, 1383, 1384],
        [1388, 1389, 1390, 1391],
        [1395, 1396, 1397, 1398],
        [1402, 1403, 1404, 1405],
        [1409, 1410, 1411, 1412]
    ]) == "Yes"
    assert solve(2, 3, [[6, 7, 8], [13, 14, 15]]) == "No"


if __name__ == "__main__":
    test()
    main()
