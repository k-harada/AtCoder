def solve(k):
    res = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(k):
        res = res + alphabet[i]
    return res


def main():
    k = int(input())
    res = solve(k)
    print(res)


def test():
    assert solve(3) == "ABC"
    assert solve(1) == "A"


if __name__ == "__main__":
    test()
    main()
