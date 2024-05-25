def solve(n):
    res_list = []
    for i in range(n):
        if i % 3 != 2:
            res_list.append("o")
        else:
            res_list.append("x")
    return "".join(res_list)


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(7) == "ooxooxo"
    assert solve(9) == "ooxooxoox"


if __name__ == "__main__":
    test()
    main()
