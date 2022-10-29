def solve(s_list):
    if "H" not in s_list:
        return "No"
    if "2B" not in s_list:
        return "No"
    if "3B" not in s_list:
        return "No"
    if "HR" not in s_list:
        return "No"
    return "Yes"


def main():
    s_list = [input() for _ in range(4)]
    res = solve(s_list)
    print(res)


def test():
    assert solve(["3B", "HR", "2B", "H"]) == "Yes"
    assert solve(["2B", "3B", "HR", "3B"]) == "No"


if __name__ == "__main__":
    test()
    main()
