def solve(n, s_list):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = [[0] * 26 for _ in range(2 ** n)]
    # j: 残っているもの
    # a: 直近の呼ばれた文字
    # res[j][a] = 0: 未決定
    # res[j][a] = 1: 手番が勝ち
    # res[j][a] = -1: 手番が負け
    count = [[] for _ in range(n + 1)]
    for j in range(2 ** n):
        count[str(bin(j)).count("1")].append(j)
    # print(count)
    for j in count[0]:
        for a in range(26):
            # 全部使い切っているので負け
            res[j][a] = -1
    for p in range(1, n + 1):
        for j in count[p]:
            for i in range(n):
                if (j >> i) & 1:
                    p = alphabet.index(s_list[i][0])
                    q = alphabet.index(s_list[i][-1])
                    if res[j ^ (1 << i)][q] == -1:
                        res[j][p] = 1
            for a in range(26):
                if res[j][a] == 0:
                    res[j][a] = -1
    if max(res[-1]) == 1:
        return "First"
    else:
        return "Second"


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
        "yucatec"
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
