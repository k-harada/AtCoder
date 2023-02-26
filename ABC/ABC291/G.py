import numpy as np


def convolve(f, g):
    """多項式 f, g の積を計算する。

    Parameters
    ----------
    f : np.ndarray (int64)
        f[i] に、x^i の係数が入っている

    g : np.ndarray (int64)
        g[i] に、x^i の係数が入っている


    Returns
    -------
    h : np.ndarray
        f,g の積
    """
    # h の長さ以上の n=2^k を計算
    fft_len = 1
    while 2 * fft_len < len(f) + len(g) - 1:
        fft_len *= 2
    fft_len *= 2

    # フーリエ変換
    Ff = np.fft.rfft(f, fft_len)
    Fg = np.fft.rfft(g, fft_len)

    # 各点積
    Fh = Ff * Fg

    # フーリエ逆変換
    h = np.fft.irfft(Fh, fft_len)

    # 小数になっているので、整数にまるめる
    h = np.rint(h).astype(np.int64)

    return h[:len(f) + len(g) - 1]


def solve(n, a_list, b_list):
    a_bit = np.zeros((5, 2 * n), dtype=np.int32)
    b_bit = np.zeros((5, n), dtype=np.int32)
    a_arr = np.array(a_list + a_list, dtype=np.int32)
    b_arr = np.array(b_list, dtype=np.int32)
    for j in range(5):
        a_bit[j, :] = (a_arr >> j) & 1
        b_bit[j, :] = (b_arr >> j) & 1
    # print(a_bit)
    # print(b_bit)
    res = [0] * n
    for j in range(5):
        conv = convolve(1 - a_bit[j, ::-1], 1 - b_bit[j, :])
        # print(n - conv)
        for i in range(n):
            res[i] += (2 ** j) * (n - conv[n + i])

    # print(res)
    return max(res)


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    print(res)


def test():
    assert solve(3, [0, 1, 3], [0, 2, 3]) == 8
    assert solve(3, [0, 0, 0], [0, 0, 0]) == 0
    assert solve(5, [1, 6, 1, 4, 3], [0, 6, 4, 0, 1]) == 23


if __name__ == "__main__":
    test()
    main()
