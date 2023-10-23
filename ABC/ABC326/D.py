from heapq import heappop, heappush


def solve(n, td_list):
    res = 0
    td_list_s = list(sorted(td_list, key=lambda x: x[0]))
    h = []
    i = 0
    t_now = 0
    while i < n or len(h):
        # print(i, t_now)
        # 時間経過
        if len(h) == 0:
            t, d = td_list_s[i]
            if t > t_now:
                t_now = t
        # 追加
        while i < n:
            t, d = td_list_s[i]
            if t == t_now:
                heappush(h, t + d)
                i += 1
            else:
                break
        # pop
        while len(h):
            t_ = heappop(h)
            if t_ >= t_now:
                res += 1
                break
        t_now += 1

    return res


def main():
    n = int(input())
    td_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, td_list)
    print(res)


def test():
    assert solve(5, [(1, 1), (1, 1), (2, 1), (1, 2), (1, 4)]) == 4
    assert solve(2, [(1, 1), (1000000000000000000, 1000000000000000000)]) == 2
    assert solve(10, [
        (4, 1), (1, 2), (1, 4), (3, 2), (5, 1),
        (5, 1), (4, 1), (2, 1), (4, 1), (2, 4)
    ]) == 6


if __name__ == "__main__":
    test()
    main()
