def solve(s):
    if len(s) % 2 == 1:
        return "No"
    for i, x in enumerate(s):
        if i % 2 == 0 and x != "h":
            return "No"
        if i % 2 == 1 and x != "i":
            return "No"
    return "Yes"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("hihi") == "Yes"
    assert solve("hi") == "Yes"
    assert solve("ha") == "No"


if __name__ == "__main__":
    test()
    main()
