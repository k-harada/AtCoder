def solve_sub(n, s):
    c = s.count("1")
    if c % 2 == 1:
        return -1
    elif c >= 4:
        return c // 2
    elif c == 0:
        return 0
    # c == 2
    ones = []
    for i in range(n):
        if s[i] == "1":
            ones.append(i)
    if ones[1] - ones[0] >= 2:
        return 1
    elif n >= 5:
        return 2
    elif n <= 3:
        return -1
    elif s == "0110":
        return 3
    else:
        return 2


def solve(t, case_list):
    res = [solve_sub(n, s) for n, s in case_list]
    return res


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
    assert solve(5, [
        (3, "101"), (6, "101101"), (5, "11111"), (6, "000000"), (30, "111011100110101100101000000111")
    ]) == [1, 2, -1, 0, 8]


if __name__ == "__main__":
    test()
    main()
