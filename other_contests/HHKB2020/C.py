from heapq import heappush, heappop


def solve(n, p_list):
    h = []
    for i in range(200002):
        heappush(h, i)
    res_list = []
    is_used = [0] * 200001
    for i in range(n):
        p = p_list[i]
        is_used[p] = 1
        while True:
            q = heappop(h)
            if is_used[q] == 0:
                res_list.append(q)
                heappush(h, q)
                break
    # print(res_list)
    return res_list


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [1, 1, 0, 2]) == [0, 0, 2, 3]
    assert solve(10, [5, 4, 3, 2, 1, 0, 7, 7, 6, 6]) == [0, 0, 0, 0, 0, 6, 6, 6, 8, 8]


if __name__ == "__main__":
    test()
    main()
