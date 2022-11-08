def solve(ab, bc, ca):
    return ab * bc // 2


def main():
    ab, bc, ca = map(int, input().split())
    res = solve(ab, bc, ca)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve(3, 4, 5) == 6
    assert solve(5, 12, 13) == 30
    assert solve(45, 28, 53) == 630


if __name__ == "__main__":
    test()
    main()
