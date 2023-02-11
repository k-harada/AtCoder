def solve(n, m, a_list):
    res = []
    temp = []
    for p in range(1, n + 1):
        if p in a_list:
            temp.append(p)
        else:
            res.append(p)
            while len(temp):
                res.append(temp.pop())
    return " ".join([str(i) for i in res])


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(5, 3, [1, 3, 4]) == "2 1 5 4 3"
    assert solve(5, 0, []) == "1 2 3 4 5"
    assert solve(10, 6, [1, 2, 3, 7, 8, 9]) == "4 3 2 1 5 6 10 9 8 7"


if __name__ == "__main__":
    test()
    main()
