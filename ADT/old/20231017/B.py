def solve(s_list):
    res = "Yes"
    for s in s_list:
        if s < 100 or s > 675:
            res = "No"
        if s % 25 != 0:
            res = "No"
    for i in range(len(s_list) - 1):
        if s_list[i] > s_list[i + 1]:
            res = "No"
    return res


def main():
    s_list = list(map(int, input().split()))
    res = solve(s_list)
    print(res)


def test():
    assert solve([125, 175, 250, 300, 400, 525, 600, 650]) == "Yes"
    assert solve([100, 250, 300, 400, 325, 575, 625, 675]) == "No"
    assert solve([0, 23, 24, 145, 301, 413, 631, 632]) == "No"


if __name__ == "__main__":
    test()
    main()
