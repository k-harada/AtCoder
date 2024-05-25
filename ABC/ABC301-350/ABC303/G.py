from collections import deque


def slide_min(a_list, k):
    n = len(a_list)
    # b_list[i] = min([a_list[i + j] for j in range(k)])
    b_list = []
    queue = deque()
    for i in range(k - 1):
        while len(queue):
            if a_list[queue[-1]] >= a_list[i]:
                queue.pop()
            else:
                break
        queue.append(i)

    for i in range(k - 1, n):
        while len(queue):
            if a_list[queue[-1]] >= a_list[i]:
                queue.pop()
            else:
                break
        queue.append(i)
        if queue[0] == i - k:
            queue.popleft()
        b_list.append(a_list[queue[0]])
    return b_list


def slide_max(a_list, k):
    n = len(a_list)
    # b_list[i] = max([a_list[i + j] for j in range(k)])
    b_list = []
    queue = deque()
    for i in range(k - 1):
        while len(queue):
            if a_list[queue[-1]] <= a_list[i]:
                queue.pop()
            else:
                break
        queue.append(i)

    for i in range(k - 1, n):
        while len(queue):
            if a_list[queue[-1]] <= a_list[i]:
                queue.pop()
            else:
                break
        queue.append(i)
        if queue[0] == i - k:
            queue.popleft()
        b_list.append(a_list[queue[0]])
    return b_list


def solve(n, a, b, c, d, x_list):
    s_list = [0]
    for x in x_list:
        s_list.append(s_list[-1] + x)
    dp_0 = [[- 10 ** 18] * (n + 1) for _ in range(n + 1)]
    dp_1 = [[10 ** 18] * (n + 1) for _ in range(n + 1)]
    # dp_0[i][j] [i, j)が残って高橋くんの手番のときの答え
    # dp_1[i][j] [i, j)が残って青木くんの手番のときの答え
    sgt_0 = [[] for _ in range(n + 1)]
    sgt_1 = [[] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(i + 1):
            dp_0[i][j] = 0
            dp_1[i][j] = 0
    for i in range(n):
        dp_0[i][i + 1] = x_list[i]
        sgt_0[1].append(2 * dp_0[i][i + 1])
        dp_1[i][i + 1] = -x_list[i]
        sgt_1[1].append(2 * dp_1[i][i + 1])
    for r in range(2, n + 1):
        for i in range(n + 1 - r):
            j = i + r
            # 左端をとる
            dp_0[i][j] = max(dp_0[i][j], dp_1[i + 1][j] + x_list[i])
            dp_1[i][j] = min(dp_1[i][j], dp_0[i + 1][j] - x_list[i])
            # 右端をとる
            dp_0[i][j] = max(dp_0[i][j], dp_1[i][j - 1] + x_list[j - 1])
            dp_1[i][j] = min(dp_1[i][j], dp_0[i][j - 1] - x_list[j - 1])
        # A円をすぬけくんに払う
        if r <= b:
            for i in range(n + 1 - r):
                j = i + r
                dp_0[i][j] = max(dp_0[i][j], s_list[j] - s_list[i] - a)
                dp_1[i][j] = min(dp_1[i][j], -(s_list[j] - s_list[i] - a))
        else:
            r_1 = slide_max(sgt_1[r - b], b + 1)
            r_0 = slide_min(sgt_0[r - b], b + 1)
            for i in range(n + 1 - r):
                j = i + r
                # print(i, j, (r - b) * n + i, (r - b) * n + j - (r - b) + 1)
                # print([sgt_1.query(i, i + 1) for i in range((r - b) * n + i, (r - b) * n + j - (r - b) + 1)])
                dp_0[i][j] = max(dp_0[i][j], (s_list[j] - s_list[i] - a) + r_1[i])
                dp_1[i][j] = min(dp_1[i][j], - (s_list[j] - s_list[i] - a) + r_0[i])
        # C円をすぬけくんに払う
        if r <= d:
            for i in range(n + 1 - r):
                j = i + r
                dp_0[i][j] = max(dp_0[i][j], s_list[j] - s_list[i] - c)
                dp_1[i][j] = min(dp_1[i][j], -(s_list[j] - s_list[i] - c))
        else:
            r_1 = slide_max(sgt_1[r - d], d + 1)
            r_0 = slide_min(sgt_0[r - d], d + 1)
            for i in range(n + 1 - r):
                j = i + r
                dp_0[i][j] = max(dp_0[i][j], s_list[j] - s_list[i] - c + r_1[i])
                dp_1[i][j] = min(dp_1[i][j], - (s_list[j] - s_list[i] - c) + r_0[i])
        # seg treeに値を記憶
        for i in range(n + 1 - r):
            sgt_0[r].append(dp_0[i][i + r] + (s_list[i + r] - s_list[i]))
            sgt_1[r].append(dp_1[i][i + r] - (s_list[i + r] - s_list[i]))
    # print(dp_0)
    # print(dp_1)
    # print(sgt_0)
    # print(sgt_1)
    return dp_0[0][n]


def main():
    n, a, b, c, d = map(int, input().split())
    x_list = list(map(int, input().split()))
    res = solve(n, a, b, c, d, x_list)
    print(res)


def test():
    assert solve(5, 10, 2, 1000000000, 1, [1, 100, 1, 1, 1]) == 90
    assert solve(10, 45, 3, 55, 4, [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 85
    assert solve(15, 796265, 10, 165794055, 1, [
        18804175, 185937909, 1934689, 18341, 68370722, 1653, 1, 2514380, 31381214, 905, 754483, 11, 5877098, 232, 31600
    ]) == 302361955


if __name__ == "__main__":
    test()
    main()
