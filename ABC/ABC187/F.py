def solve(n, m, edge_list):
    dp = [n + 1] * (2 ** n)
    dp[0] = 0
    graph = [[] for _ in range(n + 1)]
    for a, b in edge_list:
        graph[a].append(b)
        graph[b].append(a)
    reversed_edge_list = []
    for a in range(1, n):
        for b in range(a + 1, n + 1):
            if b not in graph[a]:
                reversed_edge_list.append((a, b))

    for i in range(2 ** n):
        flag = True
        for a, b in reversed_edge_list:
            d = 2 ** (a - 1) + 2 ** (b - 1)
            # print(a, b, d)
            if d & i == d:
                # print(d, i)
                flag = False
                break
        if flag:
            dp[i] = 1
    # print(dp)
    for i in range(2 ** n):
        j = i
        while j:
            if dp[i] > dp[j] + dp[i ^ j]:
                dp[i] = dp[j] + dp[i ^ j]
            j -= 1
            j &= i
    # print(dp)
    return dp[-1]


def main():
    n, m = map(int, input().split())
    edge_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, edge_list)
    print(res)


def test():
    assert solve(3, 2, [(1, 2), (1, 3)]) == 2
    assert solve(4, 6, [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]) == 1
    assert solve(18, 0, []) == 18


if __name__ == "__main__":
    test()
    main()
