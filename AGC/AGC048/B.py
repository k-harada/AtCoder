from heapq import heappop, heappush


def solve(n, a_list, b_list):

    h_even = []
    h_odd = []
    m = n // 2

    # base
    res = sum(a_list)
    for i in range(m):
        heappush(h_even, a_list[2 * i] - b_list[2 * i])
        heappush(h_odd, a_list[2 * i + 1] - b_list[2 * i + 1])

    res_max = res
    for _ in range(m):
        d_even = heappop(h_even)
        d_odd = heappop(h_odd)
        res -= d_even + d_odd
        res_max = max(res_max, res)
    return res_max


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    print(res)


def test():
    assert solve(4, [4, 2, 3, 1], [2, 3, 2, 4]) == 12
    assert solve(10, [
        866111664, 844917655, 383133839, 353498483, 472381277, 550309930, 378371075, 304570952, 955719384, 705445072
    ], [
        178537096, 218662351, 231371336, 865935868, 579910117, 62731178, 681212831, 16537461, 267238505, 318106937
    ]) == 6629738472


if __name__ == "__main__":
    test()
    main()
