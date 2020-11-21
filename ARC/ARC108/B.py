def solve(n, s):
    fox_list = []
    res = 0
    for t in s:
        if t == 'f':
            fox_list.append('f')
        elif t == 'o' and len(fox_list) > 0:
            last = fox_list.pop()
            if last == 'f':
                fox_list.append('fo')
            else:
                fox_list = []
        elif t == 'x' and len(fox_list) > 0:
            last = fox_list.pop()
            if last == 'fo':
                res += 1
            else:
                fox_list = []
        else:
            fox_list = []
    return n - 3 * res


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(6, 'icefox') == 3
    assert solve(7, 'firebox') == 7
    assert solve(48, 'ffoxoxuvgjyzmehmopfohrupffoxoxfofofoxffoxoxejffo') == 27


if __name__ == "__main__":
    test()
    main()
