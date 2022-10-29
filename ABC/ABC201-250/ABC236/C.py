def solve(n, m, s_list, t_list):
    res = []
    j = 0
    for i in range(n):
        if s_list[i] == t_list[j]:
            j += 1
            res.append("Yes")
        else:
            res.append("No")
    return res


def main():
    n, m = map(int, input().split())
    s_list = list(input().split())
    t_list = list(input().split())
    res = solve(n, m, s_list, t_list)
    for r in res:
        print(r)


def test():
    assert solve(5, 3, ["tokyo", "kanda", "akiba", "okachi", "ueno"], ["tokyo", "akiba", "ueno"]) == [
        "Yes", "No", "Yes", "No", "Yes"
    ]
    assert solve(7, 7, ["a", "t", "c", "o", "d", "e", "r"], ["a", "t", "c", "o", "d", "e", "r"]) == [
        "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"
    ]


if __name__ == "__main__":
    test()
    main()
