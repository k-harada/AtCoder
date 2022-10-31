def solve(n, a_list):
    return sum(a_list) - n


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [3, 4, 6]) == 10
    assert solve(5, [7, 46, 11, 20, 11]) == 90
    assert solve(7, [994, 518, 941, 851, 647, 2, 581]) == 4527


if __name__ == "__main__":
    test()
    main()
