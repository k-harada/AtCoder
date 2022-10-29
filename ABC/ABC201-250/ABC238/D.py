def solve(t, as_list):
    res = []
    for a, s in as_list:
        r = s - 2 * a
        b = 2 ** 60 - 1 - a
        if r & b == r:
            res.append("Yes")
        else:
            res.append("No")
    return res


def main():
    t = int(input())
    as_list = [tuple(map(int, input().split())) for _ in range(t)]
    res = solve(t, as_list)
    for r in res:
        print(r)


def test():
    assert solve(2, [(1, 8), (4, 2)]) == ["Yes", "No"]
    assert solve(4, [
        (201408139683277485, 381410962404666524), (360288799186493714, 788806911317182736),
        (18999951915747344, 451273909320288229), (962424162689761932, 1097438793187620758)
    ]) == ["No", "Yes", "Yes", "No"]


if __name__ == "__main__":
    test()
    main()
