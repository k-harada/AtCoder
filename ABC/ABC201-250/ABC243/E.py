def solve(n, m, abc_list):
    # ワーシャルフロイド法
    dist = [[10000000000000] * n for _ in range(n)]
    for a, b, c in abc_list:
        dist[a - 1][b - 1] = c
        dist[b - 1][a - 1] = c
    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] <= dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # 直通が最短距離以下の辺が削除可能
    res = 0
    for a, b, c in abc_list:
        flag = 0
        for k in range(n):
            if k == a - 1 or k == b - 1:
                continue
            if dist[a - 1][b - 1] >= dist[a - 1][k] + dist[k][b - 1]:
                flag = 1
        if flag:
            res += 1
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    abc_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, abc_list)
    print(res)


def test():
    assert solve(3, 3, [(1, 2, 2), (2, 3, 3), (1, 3, 6)]) == 1
    assert solve(5, 4, [(1, 3, 3), (2, 3, 9), (3, 5, 3), (4, 5, 3)]) == 0


if __name__ == "__main__":
    test()
    main()
