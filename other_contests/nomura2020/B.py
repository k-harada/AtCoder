def solve(t):
    res_list = []
    for st in t:
        if st == "P":
            res_list.append("P")
        else:
            res_list.append("D")
    return "".join(res_list)


def main():
    t = input()
    res = solve(t)
    print(res)


def test():
    assert solve("PD?D??P") == "PDDDDDP"
    assert solve("P?P?") == "PDPD"


if __name__ == "__main__":
    test()
    main()
