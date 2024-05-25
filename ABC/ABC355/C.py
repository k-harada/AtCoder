def solve(n, t, a_list):
    res_row = [0] * n
    res_col = [0] * n
    res_diag = [0, 0]
    for i, a in enumerate(a_list):
        r, c = (a - 1) // n, (a - 1) % n
        res_row[r] += 1
        if res_row[r] == n:
            return i + 1
        res_col[c] += 1
        if res_col[c] == n:
            return i + 1
        if r == c:
            res_diag[0] += 1
            if res_diag[0] == n:
                return i + 1
        if r + c == n - 1:
            res_diag[1] += 1
            if res_diag[1] == n:
                return i + 1
    return -1


def main():
    n, t = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, t, a_list)
    print(res)


def test():
    assert solve(3, 5, [5, 1, 8, 9, 7]) == 4
    assert solve(3, 5, [4, 2, 9, 7, 5]) == -1
    assert solve(4, 12, [13, 9, 6, 5, 2, 7, 16, 14, 8, 3, 10, 11]) == 9


if __name__ == "__main__":
    test()
    main()
