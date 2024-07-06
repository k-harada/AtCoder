def solve(s, t):
    n = len(s)
    for w in range(1, n):
        for c in range(w):
            u = ""
            i = 0
            while i * w + c < n:
                u = u + s[i * w + c]
                i += 1
            if u == t:
                return "Yes"
    return "No"


def main():
    s, t = input().split()
    res = solve(s, t)
    print(res)


def test():
    assert solve("atcoder", "toe") == "Yes"
    assert solve("beginner", "r") == "No"
    assert solve("verticalreading", "agh") == "No"


if __name__ == "__main__":
    test()
    main()
