def solve(s):
    # 条件1
    if s[0] != "A":
        return "WA"
    # 条件2
    c_index = 10
    for i in range(2, len(s) - 1):
        if s[i] == "C":
            # 2つ目を却下
            if c_index != 10:
                return "WA"
            c_index = i
    # ない場合を却下
    if c_index == 10:
        return "WA"
    # 条件3
    for i in range(1, len(s)):
        if i != c_index and s[i].upper() == s[i]:
            return "WA"
    return "AC"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("AtCoder") == "AC"
    assert solve("ACoder") == "WA"
    assert solve("AcycliC") == "WA"
    assert solve("AtCoCo") == "WA"
    assert solve("Atcoder") == "WA"


if __name__ == "__main__":
    test()
    main()
