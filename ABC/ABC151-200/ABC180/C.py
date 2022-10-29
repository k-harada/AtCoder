import math


def solve(n):
    res_list = []
    m = int(math.ceil(math.sqrt(n)))
    for i in range(1, m):
        if n % i == 0:
            res_list.append(i)
            res_list.append(n // i)
    if m * m == n:
        res_list.append(m)
    # print(m, res_list)
    return list(sorted(res_list))


def main():
    n = int(input())
    res = solve(n)
    for r in res:
        print(r)


def test():
    assert solve(6) == [1, 2, 3, 6]
    assert solve(1000000007) == [1, 1000000007]


if __name__ == "__main__":
    test()
    main()
