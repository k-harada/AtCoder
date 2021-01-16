def ab_rev(s):
    t = ""
    for ss in s:
        if ss == "A":
            t += "B"
        else:
            t += "A"
    return t


def solve(n):
    if n == 1:
        return [1, "AB"]
    res_list = ["AB"]
    for i in range(1, n):
        new_list = ["A" * (2 ** i) + "B" * (2 ** i)]
        for s in res_list:
            new_list.append(s + s)
            new_list.append(s + ab_rev(s))
        res_list = new_list
    return [2 ** n - 1] + res_list


def main():
    n = int(input())
    res_list = solve(n)
    for res in res_list:
        print(res)


def test():
    assert solve(1) == [1, "AB"]


if __name__ == "__main__":
    test()
    main()
