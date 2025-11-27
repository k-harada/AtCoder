from bisect import bisect_right


def solve(n, a_list):
    b_list = list(sorted(list(set(a_list))))
    m = len(b_list)
    res = [0] * n
    for a in a_list:
        r = m - bisect_right(b_list, a)
        res[r] += 1
    # print(res)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    for r in res:
        print(r)


def test():
    assert solve(6, [2, 7, 1, 8, 2, 8]) == [2, 1, 2, 1, 0, 0]
    assert solve(1, [1]) == [1]
    assert solve(10, [
        979861204, 57882493, 979861204, 447672230, 644706927,
        710511029, 763027379, 710511029, 447672230, 136397527
    ]) == [2, 1, 2, 1, 2, 1, 1, 0, 0, 0]


if __name__ == "__main__":
    test()
    main()
