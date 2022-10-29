import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


def scc(n, m, edge_array):
    tmp = np.ones(m, dtype=np.int32).T
    graph = csr_matrix((tmp, (edge_array[:])), (n, n))

    return connected_components(graph, directed=True, connection='strong')


def solve(n, m, k_list, a_list):
    ab_list = []
    # g = [[] for _ in range(n + 2)]
    for i in range(m):
        k = k_list[i]
        # g[0].append(a_list[i][0])
        ab_list.append((0, a_list[i][0]))
        for j in range(k - 1):
            p = a_list[i][j]
            q = a_list[i][j + 1]
            # g[p].append(q)
            ab_list.append((p, q))
        # g[a_list[i][-1]].append(n + 1)
        ab_list.append((a_list[i][-1], n + 1))
    edge_array = np.array(ab_list).T
    _, label = scc(n + 2, 2 * n + m, edge_array)
    for a, b in ab_list:
        if a == b:
            return "No"
    if np.unique(label).shape[0] == n + 2:
        return "Yes"
    else:
        return "No"


def main():
    n, m = map(int, input().split())
    k_list = []
    a_list = []
    for _ in range(m):
        k_list.append(int(input()))
        a_list.append(list(map(int, input().split())))
    res = solve(n, m, k_list, a_list)
    print(res)


def test():
    assert solve(2, 2, [2, 2], [[1, 2], [1, 2]]) == "Yes"
    assert solve(2, 2, [2, 2], [[1, 2], [2, 1]]) == "No"


if __name__ == "__main__":
    test()
    main()
