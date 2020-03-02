import numpy as np


def solve(k, q, d_list, query_list):

    res = []
    d_arr = np.array(d_list)
    for query in query_list:
        n, x, m = query
        d_arr_mod = (d_arr - 1) % m + 1
        x = x % m
        a_n1 = x + ((n - 1) // k) * d_arr_mod.sum() + d_arr_mod[:((n - 1) % k)].sum()
        res.append(n - 1 - a_n1 // m)

    return res


def main():
    k, q = map(int, input().split())
    d_list = list(map(int, input().split()))
    query_list = [map(int, input().split()) for _ in range(q)]
    res = solve(k, q, d_list, query_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 1, [3, 1, 4], [(5, 3, 2)]) == [1]
    assert solve(7, 3, [27, 18, 28, 18, 28, 46, 1000000000], [
        (1000000000, 1, 7), (1000000000, 2, 10), (1000000000, 3, 12)]) == [224489796, 214285714, 559523809]


if __name__ == "__main__":
    # test()
    main()
