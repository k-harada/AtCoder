import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


def scc(n, m, edge_array):
    tmp = np.ones(m, dtype=np.int32).T
    graph = csr_matrix((tmp, (edge_array[:])), (n, n))

    return connected_components(graph, directed=True, connection='strong')


def solve(n, m, ab_list):
    _, label = scc(n + 1, m, np.array(ab_list).T)

    res = 0
    count = [0] * (n + 1)
    for i in range(n + 1):
        count[label[i]] += 1
    for i in range(n + 1):
        res += count[i] * (count[i] - 1) // 2
    return res


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, ab_list)
    print(res)


def test():
    assert solve(4, 7, [(1, 2), (2, 1), (2, 3), (4, 3), (4, 1), (1, 4), (2, 3)]) == 3
    assert solve(100, 1, [(1, 2)]) == 0


if __name__ == "__main__":
    test()
    main()


