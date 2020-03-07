def solve(s, q, query_list):
    flag = 1
    add_right = []
    add_left = []
    for i in range(q):
        query = query_list[i]
        if len(query) == 1:
            flag *= -1
        else:
            if query[1] == "1":
                if flag == 1:
                    add_left.append(query[2])
                else:
                    add_right.append(query[2])
            else:
                if flag == 1:
                    add_right.append(query[2])
                else:
                    add_left.append(query[2])
    s = "".join(list(reversed(add_left))) + s + "".join(add_right)
    # print(s, flag)
    if flag == 1:
        return s
    else:
        return "".join(list(reversed(s)))


def main():
    s = input()
    q = int(input())
    query_list = [list(input().split()) for _ in range(q)]
    res = solve(s, q, query_list)
    print(res)


def test():
    assert solve("a", 4, [["2", "1", "p"], ["1"], ["2", "2", "c"], ["1"]]) == "cpa"
    assert solve("a", 6, [["2", "2", "a"], ["2", "1", "b"], ["1"], ["2", "2", "c"], ["1"], ["1"]]) == "aabc"
    assert solve("y", 1, [["2", "1", "x"]]) == "xy"


if __name__ == "__main__":
    test()
    main()
