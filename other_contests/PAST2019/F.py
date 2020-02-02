def solve(s):

    s_list = []

    left = 0
    for i in range(len(s) - 1):
        if s[i].upper() == s[i] and s[i + 1].upper() == s[i + 1]:
            if i > left:
                s_list.append(s[left:i + 1])
                left = i + 1
    s_list.append(s[left:])
    # print(s_list)

    s_list_u = [[s, s.upper()] for s in s_list]
    s_list_s = list(sorted(s_list_u, key=lambda x: x[1]))

    return "".join([s_list_s[i][0] for i in range(len(s_list))])


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("FisHDoGCaTAAAaAAbCAC") == "AAAaAAbCACCaTDoGFisH"
    assert solve("AAAAAjhfgaBCsahdfakGZsZGdEAA") == "AAAAAAAjhfgaBCsahdfakGGdEZsZ"


if __name__ == "__main__":
    test()
    main()
