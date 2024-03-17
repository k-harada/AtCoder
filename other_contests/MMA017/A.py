def solve(n, a_list, b_list):
    res = 0
    for a, b in zip(a_list, b_list):
        if b >= a:
            res += 1
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve(5, [1, 4, 5, 9, 2], [3, 10, 7, 6, 1]) == 3
    assert solve(1, [100], [100]) == 1


if __name__ == "__main__":
    test()
    main()
