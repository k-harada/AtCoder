def solve(r, c):
    for i in range(1, 9):
        if min(r, c) == i or max(r, c) == 16 - i:
            if i % 2 == 1:
                return "black"
            else:
                return "white"
    return ""


def main():
    r, c = map(int, input().split())
    res = solve(r, c)
    print(res)


def test():
    assert solve(3, 5) == "black"
    assert solve(4, 5) == "white"


if __name__ == "__main__":
    test()
    main()
