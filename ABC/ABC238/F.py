from collections import deque, defaultdict


MOD = 998244353


def solve(n, k, p_list, q_list):

    in_cnt = defaultdict(int)
    outs = defaultdict(list)

    for i in range(n):
        for j in range(i + 1, n):
            if p_list[i] < p_list[j] and q_list[i] < q_list[j]:
                in_cnt[i] += 1
                outs[j].append(i)
            elif p_list[i] > p_list[j] and q_list[i] > q_list[j]:
                in_cnt[j] += 1
                outs[i].append(j)

    sorted_graph = []
    queue = deque([i for i in range(n) if in_cnt[i] == 0])
    while len(queue) != 0:
        v = queue.popleft()
        sorted_graph.append(v)
        for v2 in outs[v]:
            in_cnt[v2] -= 1
            if in_cnt[v2] == 0:
                queue.append(v2)
    # print(sorted_graph)
    cnt_matrix = [[0] * (k + 1) for _ in range(n)]
    for a in list(reversed(sorted_graph)):
        # aを使う場合

        for outs[a]

    return 0


def main():
    n, k = map(int, input().split())
    p_list = list(map(int, input().split()))
    q_list = list(map(int, input().split()))
    res = solve(n, k, p_list, q_list)
    print(res)


def test():
    assert solve(4, 2, [2, 4, 3, 1], [2, 1, 4, 3]) == 0
    assert solve(33, 16, list(range(1, 34)), list(range(33, 0, -1))) == 0
    assert solve(15, 7,
                 [4, 9, 7, 5, 6, 13, 2, 11, 3, 1, 12, 14, 15, 10, 8],
                 [4, 14, 9, 12, 7, 15, 1, 2, 8, 11, 3, 5, 13, 6, 10]
                 ) == 0


if __name__ == "__main__":
    test()
    main()
