def solve(n, s_list):
    if len(set(s_list)) != len(s_list):
        return "No"
    for s in s_list:
        if s[0] not in ["H", "D", "C", "S"]:
            return "No"
        if s[1] not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
            return "No"
    return "Yes"


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    print(res)


def test():
    assert solve(4, ["H3", "DA", "D3", "SK"]) == "Yes"
    assert solve(5, ["H3", "DA", "CK", "H3", "S7"]) == "No"


if __name__ == "__main__":
    test()
    main()
