from heapq import heappush, heappop


def solve(n, lr_list):
    res = 0
    h = []
    for i in range(n):
        l, r = lr_list[i]
        heappush(h, (-l, i, "left"))
        heappush(h, (-r, i, "right"))

    fat_p_now = [0] * n
    fat_p_low = [0] * n
    r_before, i_before, _ = heappop(h)
    r_before *= -1
    while True:
        r_now, i_now, lr = heappop(h)
        r_now *= -1
        for i in range(n):
            fat_p_low[i] = min(r_now, lr_list[i][1]) - lr_list[i][0]
            if r_now < lr_list[i][1]:
                fat_p_now[i] = r_before - r_now

        if lr == "left":
            break
    return 0


def main():
    n = int(input())
    lr_list = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, lr_list)
    print(res)


def test():
    assert solve() == 0
    assert solve() == 0
    assert solve() == 0


if __name__ == "__main__":
    test()
    main()
