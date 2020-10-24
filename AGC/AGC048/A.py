def solve(t, s_list):
    res_list = []
    for s in s_list:
        if s == "a" * len(s):
            res_list.append(-1)
        elif s > "atcoder":
            res_list.append(0)
        else:
            if s[1] > "a":
                res_list.append(1)
            elif s[2] > "t":
                res_list.append(1)
            elif s[2] > "a":
                res_list.append(2)
            else:
                for i, a in enumerate(s):
                    if i >= 3:
                        if a > "t":
                            res_list.append(i - 1)
                            break
                        elif a > "a":
                            res_list.append(i)
                            break
    return res_list


def main():
    t = int(input())
    s_list = [input() for _ in range(t)]
    res = solve(t, s_list)
    for r in res:
        print(r)


def test():
    assert solve(3, ["atcodeer", "codeforces", "aaa"]) == [1, 0, -1]


if __name__ == "__main__":
    test()
    main()
