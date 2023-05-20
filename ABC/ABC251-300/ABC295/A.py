def solve(n, w_list):
    for w in w_list:
        if w in ["and", "not", "that", "the", "you"]:
            return "Yes"
    return "No"


def main():
    n = int(input())
    w_list = list(input().split())
    res = solve(n, w_list)
    print(res)


def test():
    assert solve(10, ["in", "that", "case", "you", "should", "print", "yes", "and", "not", "no"]) == "Yes"
    assert solve(10, ["in", "diesem", "fall", "sollten", "sie", "no", "und", "nicht", "yes", "ausgeben"]) == "No"


if __name__ == "__main__":
    test()
    main()
