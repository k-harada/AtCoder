def solve(t, u):
    len_t = len(t)
    len_u = len(u)
    d = len_t - len_u
    for i in range(d + 1):
        for j in range(len_u):
            if u[j] != t[j + i] and t[j + i] != "?":
                break
        else:
            return "Yes"
    return "No"


def main():
    t = input()
    u = input()
    res = solve(t, u)
    print(res)


def test():
    assert solve("tak??a?h?", "nashi") == "Yes"
    assert solve("??e??e", "snuke") == "No"
    assert solve("????", "aoki") == "Yes"


if __name__ == "__main__":
    test()
    main()
