def solve(n, x, a_list):
    return " ".join([str(a) for a in a_list if a != x])


def main():
    n, x = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, x, a_list)
    print(res)


def test():
    assert solve(5, 5, [3, 5, 6, 5, 4]) == "3 6 4"
    assert solve(3, 3, [3, 3, 3]) == ""


if __name__ == "__main__":
    test()
    main()
