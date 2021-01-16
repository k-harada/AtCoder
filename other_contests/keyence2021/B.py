from collections import defaultdict


def solve(n, k, a_list):
    count_dict = defaultdict(int)
    for a in a_list:
        count_dict[a] += 1
    res = 0
    width = k
    for i in range(n + 1):
        c = min(count_dict[i], k)
        if c < width:
            res += (width - c) * i
            width = c
    return res


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(4, 2, [0, 1, 0, 2]) == 4
    assert solve(5, 2, [0, 1, 1, 2, 3]) == 4
    assert solve(20, 4, [6, 2, 6, 8, 4, 5, 5, 8, 4, 1, 7, 8, 0, 3, 6, 1, 1, 8, 3, 0]) == 11


if __name__ == "__main__":
    test()
    main()
