from collections import deque


def solve(n, m, uv_list, k, pd_list):
    g = [[] for _ in range(n + 1)]
    for u, v in uv_list:
        g[u].append(v)
        g[v].append(u)

    dists = [n + 1] * (n + 1)
    bw = [0] * (n + 1)

    # 黒くなってもOKな辺を貪欲に黒くする
    for s in range(1, n + 1):
        dists_s = [n + 1] * (n + 1)
        dists_s[s] = 0
        queue = deque([s])
        while len(queue):
            p = queue.popleft()
            for q in g[p]:
                if dists_s[q] != n + 1:
                    continue
                dists_s[q] = dists_s[p] + 1
                queue.append(q)
        # 条件に違反しないかチェック
        flag = 1
        for p, d in pd_list:
            if dists_s[p] < d:
                flag = 0
        # 黒くする
        if flag:
            for i in range(1, n + 1):
                dists[i] = min(dists[i], dists_s[i])
            bw[s] = 1

    # 最終チェック
    flag = 1
    for p, d in pd_list:
        if dists[p] != d:
            flag = 0
    if flag:
        # print(["Yes", "".join([str(c) for c in bw[1:]])])
        return ["Yes", "".join([str(c) for c in bw[1:]])]
    else:
        # print(["No"])
        return ["No"]


def main():
    n, m = map(int, input().split())
    uv_list = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    pd_list = [tuple(map(int, input().split())) for _ in range(k)]
    res = solve(n, m, uv_list, k, pd_list)
    for r in res:
        print(r)


def test():
    assert solve(5, 5, [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5)], 2, [(1, 0), (5, 2)]) == ["Yes", "11100"]
    assert solve(5, 5, [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5)], 5, [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]) == ["No"]
    assert solve(1, 0, [], 0, []) == ["Yes", "1"]


if __name__ == "__main__":
    test()
    main()
