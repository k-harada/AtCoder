from collections import defaultdict


def solve(n, a_list):
    counter = defaultdict(int)
    for a in a_list:
        counter[a] += 1
    res = 0
    for v in counter.values():
        res += v // 2
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(6, [4, 1, 7, 4, 1, 4]) == 2
    assert solve(1, [158260522]) == 0
    assert solve(10, [295, 2, 29, 295, 29, 2, 29, 295, 2, 29]) == 4


def test_large():
    assert solve(500000, list(range(1, 500001))) == 0


if __name__ == "__main__":
    test()
    # test_large()
    main()
