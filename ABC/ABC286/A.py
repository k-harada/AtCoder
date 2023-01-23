def solve(n, p, q, r, s, a_list):
    b_list = a_list[:p - 1] + a_list[r - 1:s] + a_list[q:r - 1] + a_list[p - 1:q] + a_list[s:]
    res = " ".join([str(x) for x in b_list])
    # print(res)
    return res


def main():
    n, p, q, r, s = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, p, q, r, s, a_list)
    print(res)


def test():
    assert solve(8, 1, 3, 5, 7, [1, 2, 3, 4, 5, 6, 7, 8]) == "5 6 7 4 1 2 3 8"
    assert solve(5, 2, 3, 4, 5, [2, 2, 1, 1, 1]) == "2 1 1 2 1"
    assert solve(2, 1, 1, 2, 2, [50, 100]) == "100 50"
    assert solve(10, 2, 4, 7, 9, [22, 75, 26, 45, 72, 81, 47, 29, 97, 2]) == "22 47 29 97 72 81 75 26 45 2"


if __name__ == "__main__":
    test()
    main()
