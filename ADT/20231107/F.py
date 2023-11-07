from bisect import bisect_left


def solve(n, q, a_list, x_list):
    res = []
    a_list_s = list(sorted(a_list))
    for x in x_list:
        p = bisect_left(a_list_s, x)
        res.append(n - p)
    return res


def main():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    x_list = [int(input()) for _ in range(q)]
    res = solve(n, q, a_list, x_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 1, [100, 160, 130], [120]) == [2]
    assert solve(5, 5, [1, 2, 3, 4, 5], [6, 5, 4, 3, 2]) == [0, 1, 2, 3, 4]
    assert solve(5, 5, [804289384, 846930887, 681692778, 714636916, 957747794], [
        424238336, 719885387, 649760493, 596516650, 189641422
    ]) == [5, 3, 5, 5, 5]


if __name__ == "__main__":
    test()
    main()
