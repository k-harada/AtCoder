from collections import defaultdict
from bisect import bisect_left


def solve(w, h, n, pq_list, a, a_list, b, b_list):
    counter = defaultdict(int)
    for p, q in pq_list:
        x = bisect_left(a_list, p)
        y = bisect_left(b_list, q)
        z = x * (b + 1) + y
        counter[z] += 1
    v = list(counter.values())
    if len(v) == (a + 1) * (b + 1):
        min_ = min(v)
    else:
        min_ = 0
    max_ = max(v)

    return f"{min_} {max_}"


def main():
    w, h = map(int, input().split())
    n = int(input())
    pq_list = [tuple(map(int, input().split())) for _ in range(n)]
    a = int(input())
    a_list = list(map(int, input().split()))
    b = int(input())
    b_list = list(map(int, input().split()))
    res = solve(w, h, n, pq_list, a, a_list, b, b_list)
    print(res)


def test():
    assert solve(7, 6, 5, [
        (6, 1), (3, 1), (4, 2), (1, 5), (6, 2)
    ], 2, [2, 5], 2, [3, 4]) == "0 2"
    assert solve(4, 4, 4, [
        (1, 1), (3, 1), (1, 3), (3, 3)
    ], 1, [2], 1, [2]) == "1 1"


if __name__ == "__main__":
    test()
    main()
