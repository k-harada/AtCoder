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


def solve(s, t):
    if len(t) == 1:
        if t[0] in s:
            return 0
        else:
            return 1
    s1_arr = np.array([int(a) for a in s])
    s0_arr = np.array([1 - int(a) for a in s])
    t1_arr = np.array([int(b) for b in reversed(t)])
    t0_arr = np.array([1 - int(b) for b in reversed(t)])
    r = convolve(s1_arr, t0_arr) + convolve(s0_arr, t1_arr)
    # print(r)
    res = r[len(t) - 1:-(len(t) - 1)].min()
    return res


def main():
    s = input()
    t = input()
    res = solve(s, t)
    print(res)


def test():
    assert solve("0001", "101") == 1
    assert solve("0101010", "1010101") == 7
    assert solve("10101000010011011110", "0010011111") == 1


if __name__ == "__main__":
    test()
    main()
