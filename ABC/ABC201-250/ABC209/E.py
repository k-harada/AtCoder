from collections import deque


def solve(n, s_list):
    words = dict()
    word_no = 0
    for s in s_list:
        c_st = s[:3]
        if c_st not in words.keys():
            words[c_st] = word_no
            word_no += 1
        c_end = s[-3:]
        if c_end not in words.keys():
            words[c_end] = word_no
            word_no += 1

    g = [[] for _ in range(word_no)]
    g_inv = [[] for _ in range(word_no)]

    for s in s_list:
        c_st = s[:3]
        c_end = s[-3:]
        p, q = words[c_st], words[c_end]
        g[p].append(q)
        g_inv[q].append(p)

    status = ["Draw"] * word_no
    edge_count = [len(g[i]) for i in range(word_no)]
    queue_0 = []
    queue_1 = []

    for i in range(word_no):
        if len(g[i]) == 0:
            status[i] = "Takahashi"
            queue_0.append(i)

    # print(words)
    # print(g)

    while True:
        move = 0
        # print(status)
        for p in queue_0:
            for q in g_inv[p]:
                if status[q] == "Draw":
                    status[q] = "Aoki"
                    queue_1.append(q)
                    move += 1
        queue_0 = []

        for p in queue_1:
            for q in g_inv[p]:
                edge_count[q] -= 1
                if edge_count[q] == 0 and status[q] == "Draw":
                    status[q] = "Takahashi"
                    queue_0.append(q)
                    move += 1
        queue_1 = []

        if move == 0:
            break
    res = [status[words[s[-3:]]] for s in s_list]
    # print(res)
    return res


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    for r in res:
        print(r)


def test():
    assert solve(3, ["abcd", "bcda", "ada"]) == ["Aoki", "Takahashi", "Draw"]
    assert solve(1, ["ABC"]) == ["Draw"]
    assert solve(5, ["eaaaabaa", "eaaaacaa", "daaaaaaa", "eaaaadaa", "daaaafaa"]) == ["Takahashi", "Takahashi", "Takahashi", "Aoki", "Takahashi"]


if __name__ == "__main__":
    test()
    main()
