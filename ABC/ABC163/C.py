def solve(n, a_list):
    res_list = [0] * n
    for a in a_list:
        res_list[a - 1] += 1
    return res_list


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [1, 1, 2, 2]) == [2, 2, 0, 0, 0]
    assert solve(10, [1, 1, 1, 1, 1, 1, 1, 1, 1]) == [9, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert solve(7, [1, 2, 3, 4, 5, 6]) == [1, 1, 1, 1, 1, 1, 0]


if __name__ == "__main__":
    test()
    main()
