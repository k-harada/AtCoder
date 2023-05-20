def solve(n, a_list):
    res = []
    for a in a_list:
        if a % 2 == 0:
            res.append(a)
    return " ".join([str(r) for r in res])


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(5, [1, 2, 3, 5, 6]) == "2 6"
    assert solve(5, [2, 2, 2, 3, 3]) == "2 2 2"
    assert solve(10, [22, 3, 17, 8, 30, 15, 12, 14, 11, 17]) == "22 8 30 12 14"


if __name__ == "__main__":
    test()
    main()
