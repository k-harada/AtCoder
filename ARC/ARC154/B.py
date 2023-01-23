def solve(n, s, t):

    if list(sorted(list(s))) != list(sorted(list(t))):
        return -1

    res = n
    j = n - 1
    first_count = s.count(t[0])
    for i in range(n - 1, -1, -1):
        while s[i] != t[j] and j >= 0:
            j -= 1
        # print(i, j, s[i], t[j])
        if j < 0:
            break
        if s[i] == t[0]:
            first_count -= 1
        res = i
        j -= 1
    # print(res)
    return res


def main():
    n = int(input())
    s = input()
    t = input()
    res = solve(n, s, t)
    print(res)


def test():
    assert solve(4, "abab", "abba") == 2
    assert solve(3, "arc", "cra") == 2


if __name__ == "__main__":
    test()
    main()
