def solve(a, b):
    a_list = [i + 1 for i in range(a)]
    b_list = [-(i + 1) for i in range(b)]
    if a > b:
        b_list[-1] = - sum(a_list) - sum(b_list[:-1])
    elif a < b:
        a_list[-1] = - sum(b_list) - sum(a_list[:-1])

    return " ".join([str(p) for p in a_list + b_list])


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(1, 1) == "1 -1"
    assert solve(1, 4) == "10 -1 -2 -3 -4"
    assert solve(7, 5) == "1 2 3 4 5 6 7 -1 -2 -3 -4 -18"


if __name__ == "__main__":
    test()
    main()
