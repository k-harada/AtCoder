def solve(xs):
    if "." in xs:
        return int(xs[:xs.index(".")])
    else:
        return int(xs)


def main():
    xs = input()
    res = solve(xs)
    print(res)


def test():
    assert solve("5.90") == 5
    assert solve("0") == 0
    assert solve("84939825309432908832902189.9092309409809091329") == 84939825309432908832902189


if __name__ == "__main__":
    test()
    main()
