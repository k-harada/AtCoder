def solve(n, s):
    res_list = []
    flag = 0
    for i, c in enumerate(s):
        if c == '"':
            flag = 1 - flag
        if c == "," and flag == 0:
            res_list.append(".")
        else:
            res_list.append(c)
    return "".join(res_list)


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(8, '"a,b"c,d') == '"a,b"c.d'
    assert solve(5, ',,,,,') == '.....'
    assert solve(20, 'a,"t,"c,"o,"d,"e,"r,') == 'a."t,"c."o,"d."e,"r.'


if __name__ == "__main__":
    test()
    main()
