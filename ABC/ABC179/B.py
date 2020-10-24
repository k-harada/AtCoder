def solve(n, d_list):
    straight = 0
    for i in range(n):
        d1, d2 = d_list[i]
        if d1 == d2:
            straight += 1
            if straight == 3:
                return "Yes"
        else:
            straight = 0
    return "No"


def main():
    n = int(input())
    d_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, d_list)
    print(res)


def test():
    assert solve(5, [(1, 2), (6, 6), (4, 4), (3, 3), (2, 2)]) == "Yes"
    assert solve(5, [(1, 1), (2, 2), (3, 4), (5, 5), (6, 6)]) == "No"
    assert solve(6, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]) == "Yes"


if __name__ == "__main__":
    test()
    main()
