def scc(n, ab_list):  # 非再帰関数で実装

    g = [[] for _ in range(n + 1)]
    g_rev = [[] for _ in range(n + 1)]
    for a, b in ab_list:
        g[a].append(b)
        g_rev[b].append(a)

    def dfs(v):
        stack = [v]
        used[v] = True
        while len(stack) != 0:
            tmp = stack[-1]
            flag = True
            for i in g[tmp]:
                if not used[i]:
                    flag = False
                    used[i] = True
                    stack.append(i)
                    break
            if flag:  # どこにも行かなかった時
                stack.pop()
                # stack = stack[:-1] #一行上に最適化
                vs.append(tmp)

    def rdfs(v, k):
        stack = [v]
        used[v] = True
        cmp[v] = k
        while len(stack) != 0:
            tmp = stack[-1]
            stack.pop()
            # stack = stack[:-1] #一行上に最適化
            used[tmp] = True
            for i in g_rev[tmp]:
                if not used[i]:
                    cmp[i] = k
                    stack.append(i)

    used = [False] * n  # 既に調べたかどうか
    vs = []  # 帰りがけの並び
    cmp = [-1] * n
    for i in range(n):
        if not used[i]:
            dfs(i)
    k = 0
    used = [False] * n  # 既に調べたかどうか
    for i in vs[::-1]:
        if not used[i]:
            rdfs(i, k)
            k += 1
    return k, cmp  # 強連結成分分解をしたあとの要素数kとそれぞれの点がどこに位置するか


def solve(n, m, ab_list):
    _, label = scc(n + 1, ab_list)

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
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(4, 7, [(1, 2), (2, 1), (2, 3), (4, 3), (4, 1), (1, 4), (2, 3)]) == 3
    assert solve(100, 1, [(1, 2)]) == 0


if __name__ == "__main__":
    test()
    main()
