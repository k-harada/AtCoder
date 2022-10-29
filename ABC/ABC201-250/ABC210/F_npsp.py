from collections import defaultdict
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


def scc(n, m, edge_array):
    tmp = np.ones(m, dtype=np.int32).T
    graph = csr_matrix((tmp, (edge_array[:])), (n, n))

    return connected_components(graph, directed=True, connection='strong')


def solve(n, ab_list):

    small_primes_flag = [1] * 2000
    small_primes_flag[0] = 0
    small_primes_flag[1] = 0

    for p in range(2000):
        if small_primes_flag[p] and p * p < 2000:
            for q in range(p * p, 2000, p):
                small_primes_flag[q] = 0
    small_primes = [p for p in range(2000) if small_primes_flag[p]]
    i = 0
    dict_list = [defaultdict(int) for _ in range(n)]
    for a, b in ab_list:
        a_ = a
        b_ = b
        for p in small_primes:
            if a % p == 0:
                dict_list[i][p] += 1
                while a_ % p == 0:
                    a_ //= p
            if b % p == 0:
                dict_list[i][p] += 2
                while b_ % p == 0:
                    b_ //= p
        if a_ > 1:
            dict_list[i][a_] += 1
        if b_ > 1:
            dict_list[i][b_] += 2
        i += 1

    # graph
    node_name = 2 * n
    past_node_name = [0] * 2000000
    cd_list = []
    for i in range(n):
        for p in dict_list[i].keys():
            past_node = past_node_name[p]
            if dict_list[i][p] == 1:
                cd_list.append((2 * i, node_name))
                cd_list.append((node_name + 1, 2 * i + 1))
                if past_node > 0:
                    cd_list.append((2 * i, past_node + 1))
                    cd_list.append((past_node, 2 * i + 1))
            elif dict_list[i][p] == 2:
                cd_list.append((2 * i + 1, node_name))
                cd_list.append((node_name + 1, 2 * i))
                if past_node > 0:
                    cd_list.append((2 * i + 1, past_node + 1))
                    cd_list.append((past_node, 2 * i))
            elif dict_list[i][p] == 3:
                cd_list.append((2 * i, node_name))
                cd_list.append((2 * i + 1, node_name))
                cd_list.append((node_name + 1, 2 * i))
                cd_list.append((node_name + 1, 2 * i + 1))
                if past_node > 0:
                    cd_list.append((2 * i, past_node + 1))
                    cd_list.append((2 * i + 1, past_node + 1))
                    cd_list.append((past_node, 2 * i))
                    cd_list.append((past_node, 2 * i + 1))
            if past_node > 0:
                cd_list.append((past_node, node_name))
                cd_list.append((node_name + 1, past_node + 1))
            past_node_name[p] = node_name
            node_name += 2
    # print(cd_list)
    if len(cd_list) > 0:
        _, label = scc(node_name, len(cd_list), np.array(cd_list).T)
    else:
        label = list(range(node_name))

    # print(label)
    for i in range(0, node_name, 2):
        if label[i] == label[i + 1]:
            return "No"
    return "Yes"


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(3, [(2, 5), (10, 9), (4, 8)]) == "Yes"
    assert solve(2, [(10, 100), (1000, 10000)]) == "No"


if __name__ == "__main__":
    test()
    main()
