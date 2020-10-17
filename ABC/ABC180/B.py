import math


def solve(n, x_list):

    d1 = sum([abs(x) for x in x_list])
    d2 = math.sqrt(sum([x ** 2 for x in x_list]))
    d3 = max([abs(x) for x in x_list])

    return [d1, d2, d3]


def main():
    n = int(input())
    x_list = list(map(int, input().split()))
    res = solve(n, x_list)
    for r in res:
        print(r)


def test():
    print(solve(2, [2, -1]))
    print(solve(10, [3, -1, -4, 1, -5, 9, 2, -6, 5, -3]))


if __name__ == "__main__":
    # test()
    main()
