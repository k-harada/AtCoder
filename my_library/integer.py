from subprocess import Popen, PIPE


# from nagiss-san's AC
def fast_prime_factorization(n):
    # 素因数分解（ロー法）  O(n^(1/4) polylog(n))
    return list(map(int, Popen(["factor", str(n)], stdout=PIPE).communicate()[0].split()[1:]))


import numpy as np


def calc_div(n):
    sq = int(n**.5 + 10)
    x = np.arange(1, sq)
    x = x[n % x == 0]
    x = np.concatenate((x, n // x))
    return np.unique(x)
