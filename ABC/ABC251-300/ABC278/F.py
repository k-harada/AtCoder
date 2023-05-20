def solve(n, s_list):

    # i にいて、既に使われているものがk
    g_forward = [[] for _ in range(n * (2 ** n))]
    g_backward = [[] for _ in range(n * (2 ** n))]
    # graph
    for i in range(n):
        # 移動可能なjのリスト
        j_list = []
        for j in range(n):
            if i != j and s_list[i][-1] == s_list[j][0]:
                j_list.append(j)
        for k in range(2 ** n):
            # そもそも矛盾している
            if (2 ** i) & k == 0:
                continue
            p = i * (2 ** n) + k
            # 移動可能なj
            for j in j_list:
                if (2 ** j) & k == 0:
                    q = j * (2 ** n) + k + 2 ** j
                    g_forward[p].append(q)
                    g_backward[q].append(p)
    status = [-1] * (n * (2 ** n))
    k_order = [[] for _ in range(n + 1)]
    for k in range(2 ** n):
        c = str(bin(k)).count("1")
        k_order[c].append(k)

    for c in range(n, -1, -1):
        for k in k_order[c]:
            for i in range(n):
                p = i * (2 ** n) + k
                # 行き先がないなら、その状態で手番の勝利
                if status[p] == -1:
                    status[p] = 1
                for q in g_backward[p]:
                    # qの次にpを言われたら負け
                    if status[p] == 1:
                        status[q] = 0
    res = "Second"
    for i in range(n):
        if status[i * (2 ** n) + (2 ** i)] == 1:
            res = "First"
    # print(res)
    return res


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    print(res)


def test():
    assert solve(6, ["enum", "float", "if", "modint", "takahashi", "template"]) == "First"
    assert solve(10, [
        "catch",
        "chokudai",
        "class",
        "continue",
        "copy",
        "exec",
        "havoc",
        "intrinsic",
        "static",
        "yucatec",
    ]) == "Second"
    assert solve(16, [
        "mnofcmzsdx",
        "lgeowlxuqm",
        "ouimgdjxlo",
        "jhwttcycwl",
        "jbcuioqbsj",
        "mdjfikdwix",
        "jhvdpuxfil",
        "peekycgxco",
        "sbvxszools",
        "xuuqebcrzp",
        "jsciwvdqzl",
        "obblxzjhco",
        "ptobhnpfpo",
        "muizaqtpgx",
        "jtgjnbtzcl",
        "sivwidaszs",
    ]) == "First"


if __name__ == "__main__":
    # test()
    main()
