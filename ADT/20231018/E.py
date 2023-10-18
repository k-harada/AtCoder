def solve(s):
    n = len(s)
    # 右のaの数
    right = 0
    for i in range(n - 1, -1, -1):
        if s[i] == "a":
            right += 1
        else:
            break
    # 左のaの数
    left = 0
    for i in range(n):
        if s[i] == "a":
            left += 1
        else:
            break
    if left < right:
        s_ = "a" * (right - left) + s
    else:
        s_ = s
    # print(s_)
    # 回文チェック
    res = "Yes"
    m = len(s_)
    for i in range(m):
        if s_[i] != s_[m - 1 - i]:
            res = "No"
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("kasaka") == "Yes"
    assert solve("atcoder") == "No"
    assert solve("php") == "Yes"


if __name__ == "__main__":
    test()
    main()
