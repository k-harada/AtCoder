def solve(n, k, s):
    while k > 0:
        if len(s) % 2 == 1:
            s = s + s
        t = ""
        for i in range(0, len(s), 2):
            a = s[i]
            b = s[i + 1]
            if a == 'R':
                if b == 'P':
                    t += 'P'
                else:
                    t += 'R'
            elif a == 'S':
                if b == 'R':
                    t += 'R'
                else:
                    t += 'S'
            else:
                if b == 'S':
                    t += 'S'
                else:
                    t += 'P'
        k -= 1
        s = t
    return s[0]


def main():
    n, k = map(int, input().split())
    s = input()
    res = solve(n, k, s)
    print(res)


def test():
    assert solve(3, 2, 'RPS') == 'P'
    assert solve(11, 1, 'RPSSPRSPPRS') == 'P'
    assert solve(1, 100, 'S') == 'S'


if __name__ == "__main__":
    test()
    main()
