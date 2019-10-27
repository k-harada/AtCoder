import numpy as np
from scipy.sparse.csgraph import floyd_warshall


def main():
    n, m, le = map(int, input().split())
    g1 = (le + 1) * np.zeros((n, n))
    for _ in range(m):
        a, b, c = map(int, input().split())
        if c <= le:
            g1[a - 1, b - 1] = c
            g1[b - 1, a - 1] = c

    fw1 = floyd_warshall(g1, directed=False)

    g2 = 1000 * np.zeros((n, n))
    g2[fw1 <= le] = 1

    fw2 = floyd_warshall(g2, directed=False)

    q = int(input())
    res_list = [-1] * q
    for i in range(q):
        s, t = map(int, input().split())
        res = fw2[s - 1, t - 1]
        if res <= n:
            res_list[i] = int(res - 1)

    for r in res_list:
        print(r)


if __name__ == "__main__":
    main()
