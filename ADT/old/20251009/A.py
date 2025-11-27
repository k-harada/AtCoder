def solve(s):
    if 200 <= s < 300:
        return "Success"
    else:
        return "Failure"


def main():
    s = int(input())
    res = solve(s)
    print(res)


def test():
    assert solve(200) == "Success"
    assert solve(401) == "Failure"
    assert solve(999) == "Failure"


if __name__ == "__main__":
    test()
    main()
