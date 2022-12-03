def solve(h, w, s):
    res = 0
    for row in s:
        res += row.count("#")
    return res


def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    res = solve(h, w, s)
    print(res)


def test():
    assert solve(3, 5, [
        "#....",
        ".....",
        ".##.."
    ]) == 3
    assert solve(1, 10, [".........."]) == 0


if __name__ == "__main__":
    test()
    main()
