def solve(n, m, a_list):
    wait = []
    res = []
    for i in range(1, n + 1):
        wait.append(i)
        if i not in a_list:
            while len(wait):
                res.append(wait.pop())
    while len(wait):
        res.append(wait.pop())
    # print(res)
    return " ".join([str(a) for a in res])


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
