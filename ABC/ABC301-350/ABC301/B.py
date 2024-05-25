def solve(n, a_list):
    res = []
    for i in range(n - 1):
        if a_list[i] < a_list[i + 1]:
            for j in range(a_list[i], a_list[i + 1]):
                res.append(j)
        else:
            for j in range(a_list[i], a_list[i + 1], -1):
                res.append(j)
    res.append(a_list[-1])
    return " ".join([str(r) for r in res])


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(4, [2, 5, 1, 2]) == "2 3 4 5 4 3 2 1 2"
    assert solve(6, [3, 4, 5, 6, 5, 4]) == "3 4 5 6 5 4"


if __name__ == "__main__":
    test()
    main()
