def solve(n, k, x, a_list):
    res = a_list[:k] + [x] + a_list[k:]
    return " ".join([str(r) for r in res])


def main():
    n, k, x = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, x, a_list)
    print(res)


def test():
    assert solve(4, 3, 7, [2, 3, 5, 11]) == "2 3 5 7 11"
    assert solve(1, 1, 100, [100]) == "100 100"
    assert solve(8, 8, 3, [9, 9, 8, 2, 4, 4, 3, 5]) == "9 9 8 2 4 4 3 5 3"


if __name__ == "__main__":
    test()
    main()
