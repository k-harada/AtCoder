def solve_sub(n, s):
    for i in range(1, n):
        if s[:i] < s[i:]:
            return "Yes"
    return "No"


def solve(t, case_list):
    return [solve_sub(n, s) for n, s in case_list]


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        n = int(input())
        s = input()
        case_list.append((n, s))
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve_sub(4, "abac") == "Yes"
    assert solve_sub(3, "cac") == "No"
    assert solve_sub(2, "ab") == "Yes"
    assert solve_sub(5, "edcba") == "No"


def test_large():
    assert solve_sub(2000, "b" + "a" * 1999) == "No"


if __name__ == "__main__":
    test()
    # test_large()
    main()
