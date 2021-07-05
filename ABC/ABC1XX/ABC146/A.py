def solve(s):
    return 7 - ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"].index(s)


def main():
    s = input()
    print(solve(s))


def test():
    assert solve("SAT") == 1
    assert solve("SUN") == 7


if __name__ == "__main__":
    main()
