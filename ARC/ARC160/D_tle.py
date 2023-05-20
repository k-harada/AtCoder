import numpy as np


MOD = 998244353


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


def convolve2(f, g, p):
    """多項式f, gの積をmod pで計算する。
    小数を経由するため計算誤差が生じるが、pが10^9程度、
    f, gの長さが250000以下程度であれば、正確な計算ができる"""
    # f = 2^15 f_1 + f_2　などと分解
    f1, f2 = np.divmod(f, 1 << 15)
    g1, g2 = np.divmod(g, 1 << 15)

    # h = 2^30 a + 2^15 b + c となるa, b, cを計算する
    # bについては、b = f1g2 + f2g1 = (f1 + f2)(g1 + g2) - (f1g1 + f2g2)を利用
    a = convolve(f1, g1) % p
    c = convolve(f2, g2) % p
    b = (convolve(f1 + f2, g1 + g2) - (a + c)) % p

    h = (a << 30) + (b << 15) + c
    return h % p


def solve(n, m, k):
    if m % k != 0:
        return 0

    size = n
    factorial = [1] * (size + 1)
    factorial_inv = [1] * (size + 1)
    for i in range(1, size + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD

    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)

    for i in range(size, 0, -1):
        factorial_inv[i - 1] = (factorial_inv[i] * i) % MOD

    x = np.ones(k)
    v = n - k + 1
    if v & 1:
        r = np.ones(k)
    else:
        r = np.ones(1)
    for q in range(10):
        x = convolve2(x, x, MOD)
        if (v >> (q + 1)) & 1:
            r = convolve2(r, x, MOD)
    # print(r)
    p = m // k
    res = 0

    # print(r)
    h = factorial_inv[n - 1]
    for j in range(n - 1):
        h *= ((n - 1 + p) - j) % MOD
        h %= MOD
    for i in range(min(p + 1, (k - 1) * (n - k + 1) + 1)):
        if i > 0:
            h *= pow(n + p - i, MOD - 2, MOD)
            h *= (p + 1 - i) % MOD
            h %= MOD
        res += r[i] * h
        res %= MOD
        # print(res)
    return res


def main():
    n, m, k = map(int, input().split())
    res = solve(n, m, k)
    print(res)


def test():
    assert solve(3, 2, 2) == 5
    assert solve(100, 998244353, 100) == 0
    assert solve(2000, 545782618661124208, 533) == 908877889


def test_large():
    print(solve(2050, 10000000000, 4))


if __name__ == "__main__":
    # test()
    # test_large()
    main()
