def solve(s):
    s_list = []
    res = 0
    for c in s:
        if c == "A":
            s_list.append("A")
        elif c == "B":
            while len(s_list):
                d = s_list.pop()
                if d == "A":
                    s_list.append("AB")
                    break
                elif d == "AB":
                    continue
                else:
                    continue
            if len(s_list) == 0:
                res += 1
        else:
            while len(s_list):
                d = s_list.pop()
                if d == "AB":
                    s_list.append("ABC")
                    break
                elif d == "A":
                    continue
            if len(s_list) == 0:
                res += 1
    print(res)
    return res


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        res = solve(s)
        print(res)
    

def test():
    assert solve("CAABCB") == 1
    assert solve("B") == 1
    assert solve("AAABBC") == 0
    assert solve("AABBCC") == 1
    assert solve("CABCCBCBAABCBBBAABAABACABBC") == 7


if __name__ == "__main__":
    test()
    main()
