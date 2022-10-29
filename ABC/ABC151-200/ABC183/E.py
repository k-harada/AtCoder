MOD = 10 ** 9 + 7


def solve(h, w, s):
    row_cum_sum = [0] * h
    col_cum_sum = [0] * w
    diagonal_cum_sum = [0] * (h + w)

    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                c = row_cum_sum[i] + col_cum_sum[j] + diagonal_cum_sum[i - j]
                if i == 0 and j == 0:
                    c = 1
                if i == h - 1 and j == w - 1:
                    return c % MOD
                row_cum_sum[i] += c
                col_cum_sum[j] += c
                diagonal_cum_sum[i - j] += c
                row_cum_sum[i] %= MOD
                col_cum_sum[j] %= MOD
                diagonal_cum_sum[i - j] %= MOD
            else:
                row_cum_sum[i] = 0
                col_cum_sum[j] = 0
                diagonal_cum_sum[i - j] = 0
    return 0


def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    res = solve(h, w, s)
    print(res)


def test():
    assert solve(3, 3, ['...', '.#.', '...']) == 10
    assert solve(4, 4, ['...#', '....', '..#.', '....']) == 84
    assert solve(8, 10, [
        '..........', '..........', '..........', '..........', '..........', '..........', '..........', '..........'
    ]) == 13701937


if __name__ == "__main__":
    test()
    main()
