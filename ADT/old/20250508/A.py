def solve(n, k, a_list):
    res_list = []
    for a in a_list:
        if a % k == 0:
            res_list.append(a // k)
    return " ".join([str(r) for r in res_list])


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(5, 2, [2, 5, 6, 7, 10]) == "1 3 5"
    assert solve(3, 1, [3, 4, 7]) == "3 4 7"
    assert solve(5, 10, [50, 51, 54, 60, 65]) == "5 6"


if __name__ == "__main__":
    test()
    main()
