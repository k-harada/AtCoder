def solve(s):
    start = s.find("(")
    if start == -1:
        return s
    else:
        depth = 1
        for j in range(start + 1, len(s)):
            if s[j] == ")" and depth == 1:
                end = j
                break
            elif s[j] == ")":
                depth -= 1
            elif s[j] == "(":
                depth += 1
        # print(s, start, end)
        s0 = solve(s[start + 1:end])
        return solve(s[:start] + s0 + "".join(reversed(s0)) + s[end + 1:])


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("(ab)c") == "abbac"
    assert solve("past") == "past"
    # print(solve("(d(abc)e)()"))
    assert solve("(d(abc)e)()") == "dabccbaeeabccbad"
    # solve("aa()")


if __name__ == "__main__":
    test()
    main()
