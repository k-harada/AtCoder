from heapq import heappush, heappop


def solve(x, y, a, b, c, p_list, q_list, r_list):
    res = sum(p_list[:x]) + sum(q_list[:y])
    res_max = res
    # print(res)
    h = []
    for i in range(x):
        heappush(h, p_list[i])
    for j in range(y):
        heappush(h, q_list[j])
    for i in range(min(x + y, c)):
        d = heappop(h)
        res -= d
        res += r_list[i]
        res_max = max(res, res_max)
        # print(res)

    return res_max


def main():
    x, y, a, b, c = map(int, input().split())
    p_list = list(sorted(list(map(int, input().split())), reverse=True))
    q_list = list(sorted(list(map(int, input().split())), reverse=True))
    r_list = list(sorted(list(map(int, input().split())), reverse=True))
    res = solve(x, y, a, b, c, p_list, q_list, r_list)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve(1, 2, 2, 2, 1, [4, 2], [5, 1], [3]) == 12
    assert solve(2, 2, 2, 2, 2, [8, 6], [9, 2], [2, 1]) == 25
    assert solve(2, 2, 4, 4, 4, [14, 13, 12, 11], [24, 23, 22, 21], [4, 3, 2, 1]) == 74


if __name__ == "__main__":
    test()
    main()
