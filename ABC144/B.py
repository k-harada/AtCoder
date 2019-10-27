def solve_b(c):
    res = "No"
    for a in range(1, 10):
        if c % a == 0 and c // a < 10:
            res = "Yes"
    return res


def main():
    # input
    c = int(input())
    res = solve_b(c)
    print(res)


def test():
    assert solve_b(10) == "Yes"
    assert solve_b(50) == "No"
    assert solve_b(81) == "Yes"


if __name__ == "__main__":
    test()
    main()
