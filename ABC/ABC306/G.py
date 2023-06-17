from collections import deque, defaultdict


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


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def solve_sub(n, m, uv_list):
    res = "No"
    _, cmp = scc(n + 1, uv_list)
    k = cmp[1]
    g = [[] for _ in range(n + 1)]
    for u, v in uv_list:
        if cmp[u] == cmp[v] == k:
            g[u].append(v)
    queue = deque()
    queue.append(1)
    d_list = [10 ** 10] * (n + 1)
    d_list[1] = 0
    dd = 0
    while len(queue):
        p = queue.popleft()
        if 0 < d_list[p] < 10 ** 10:
            continue
        for q in g[p]:
            if d_list[q] == 10 ** 10:
                d_list[q] = d_list[p] + 1
                queue.append(q)
            else:
                d = d_list[p] + 1 - d_list[q]
                dd = gcd(dd, d)
    while dd % 2 == 0:
        dd //= 2
    while dd % 5 == 0:
        dd //= 5
    if dd == 1:
        return "Yes"
    else:
        return "No"


def solve(t, case_list):
    return [solve_sub(n, m, uv_list) for n, m, uv_list in case_list]


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        n, m = map(int, input().split())
        uv_list = [tuple(map(int, input().split())) for _ in range(m)]
        case_list.append((n, m, uv_list))
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve_sub(2, 2, [(1, 2), (2, 1)]) == "Yes"
    assert solve_sub(3, 3, [(1, 2), (2, 3), (3, 1)]) == "No"
    assert solve_sub(7, 10, [
        (1, 6), (6, 3), (1, 4), (5, 1), (7, 1),
        (4, 5), (2, 1), (4, 7), (2, 7), (4, 3)
    ]) == "No"
    assert solve_sub(7, 11, [
        (1, 6), (6, 3), (1, 4), (5, 1), (7, 1),
        (4, 5), (2, 1), (4, 7), (2, 7), (4, 3), (3, 7)
    ]) == "Yes"


if __name__ == "__main__":
    test()
    main()
