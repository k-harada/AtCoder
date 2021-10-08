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


# typical90 037
def solve(w, n, lrv_list):
    dp = [[0] + [-1] * w for _ in range(n + 1)]

    # slide_min
    for i in range(n):
        l, r, v = lrv_list[i]
        d = min(r - l + 1, w + 1)
        sm = slide_max([-1] * (d - 1) + dp[i] + [-1] * (d - 1), d)
        for j in range(w + 1):
            if j - l < 0:
                add = -1
            elif sm[j - l] < 0:
                add = -1
            else:
                add = v + sm[j - l]
            dp[i + 1][j] = max(dp[i][j], add)
    res = dp[-1][-1]
    # print(dp)
    return res


def main():
    w, n = map(int, input().split())
    lrv_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(w, n, lrv_list)
    print(res)


def test_min():
    assert slide_min([1, 2, 3, 4, 5], 2) == [1, 2, 3, 4]
    assert slide_min([5, 4, 3, 2, 1], 2) == [4, 3, 2, 1]
    assert slide_min([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 4) == [1, 1, 1, 1, 2, 2, 2]
    assert slide_max([1, 2, 3, 4], 4) == [4]


def test():
    assert solve(100, 4, [(30, 40, 120), (30, 40, 30), (30, 40, 1500), (30, 40, 40)]) == 1660
    assert solve(100, 4, [(13, 15, 31415), (12, 13, 92653), (29, 33, 58979), (95, 98, 32384)]) == -1
    assert solve(5000, 5, [
        (1000, 1000, 1000000000), (1000, 1000, 1000000000), (1000, 1000, 1000000000),
        (1000, 1000, 1000000000), (1000, 1000, 1000000000)
    ]) == 5000000000


if __name__ == "__main__":
    test_min()
    test()
    main()
