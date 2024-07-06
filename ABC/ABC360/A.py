def solve(s):
    rice = s.index("R")
    soup = s.index("M")
    if rice < soup:
        return "Yes"
    else:
        return "No"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("RSM") == "Yes"
    assert solve("SMR") == "No"


if __name__ == "__main__":
    test()
    main()
