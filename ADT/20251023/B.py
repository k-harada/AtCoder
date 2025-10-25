d = dict()
d["red"] = "SSS"
d["blue"] = "FFF"
d["green"] = "MMM"


def solve(s):
    if s in d.keys():
        return d[s]
    else:
        return "Unknown"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("red") == "SSS"
    assert solve("atcoder") == "Unknown"


if __name__ == "__main__":
    test()
    main()
