def solve(k):
    return "ACL" * k


def main():
    k = int(input())
    res = solve(k)
    print(res)


def test():
    assert solve(3) == "ACLACLACL"


if __name__ == "__main__":
    test()
    main()
