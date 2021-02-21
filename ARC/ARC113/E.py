from heapq import heappop, heappush, heapify


def solve_sub_0(s):
    a_count = 0
    b_count = 0
    for c in s:
        if c == "a":
            a_count += 1
        else:
            b_count += 1
    if a_count % 2 == 1 and b_count > 3:
        if s[-3:] == "bbb":
            target = -1
            for i in range(len(s) - 2):
                if s[i:i + 3] == "baa":
                    target = i
                    break
                if s[i:i + 2] == "ba":
                    target = i
            if target != -1:
                return s[:target] + "".join(list(reversed(s[target + 1:-1])))
    return s


def solve_sub_1(s):
    # find first a and last a
    first_a = 10 ** 6
    last_a = -1
    a_count = 0
    for i, c in enumerate(s):
        if c == "a":
            first_a = min(i, first_a)
            last_a = i
            a_count += 1
    # all b or only one a
    if a_count < 2:
        return s
    # a_blocks
    a_blocks = []
    a_cnt = 0
    b_count = 0
    last_add = 0
    for i, c in enumerate(s):
        if c == "a":
            a_cnt += 1
        else:
            if a_cnt > 0:
                a_blocks.append(a_cnt)
            a_cnt = 0
            if first_a < i < last_a:
                b_count += 1
    if a_cnt > 0:
        a_blocks.append(a_cnt)
    # print(a_blocks)
    a_blocks[-1] = 10 ** 6
    heapify(a_blocks)
    cnt_act = 0
    while len(a_blocks) > 1:
        m1 = heappop(a_blocks)
        m2 = heappop(a_blocks)
        cnt_act += 1
        if m1 + m2 > 2:
            heappush(a_blocks, m1 + m2 - 2)
    # false
    return s[:first_a] + "b" * b_count + "a" * (a_count - 2 * cnt_act) + s[last_a + 1:]


def solve_sub_2(s_1):
    a_count = 0
    b_count = 0
    for c in s_1:
        if c == "a":
            a_count += 1
        else:
            b_count += 1
    if s_1[0] == "a" and s_1[-1] == "b":
        if a_count % 2 == 0:
            return "b" * b_count
        else:
            return "a" + "b" * b_count
    elif s_1[0] == "b" and s_1[-1] == "b":
        if a_count % 2 == 0:
            return "b" * b_count
        elif s_1[-3:] == "bbb":
            return "b" * (b_count - 2) + "a" * a_count
        else:
            k = s_1.index("a")
            return "b" * k + "a" + "b" * (b_count - k)
    return s_1


def solve(t, s_list):
    res_list = []
    for s in s_list:
        s_0 = solve_sub_0(s)
        s_1 = solve_sub_1(s_0)
        s_2 = solve_sub_2(s_1)
        res_list.append(s_2)
        # print(s_2)
    return res_list


def main():
    t = int(input())
    s_list = [input() for _ in range(t)]
    res_list = solve(t, s_list)
    for res in res_list:
        print(res)


def test():
    assert solve(20, [
        "abbaa",
        "babbb",
        "aabbabaa",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
        "bbabaaaaabbaababaaabbabbbbbaaaaa",
        "babbbaaaabaababbbabaabaaaaababaa",
        "bbaababababbbaaabaabababaabbabab",
        "abaabbabaabaaaaabaaaabbaabaaaaab",
        "aabababbabbabbabbaaaabbabbbabaab",
        "aabababbabbbbaaaabbaaaaabbaaaabb",
        "abbbbaabaaabababaaaababababbaabb",
        "aaaaaaaaaaaaaaaaaaaaaaabbbbbbbbb",
        "aaaaaaaaaabbbbbbbbbbbbbbbbbbbbbb",
        "abababaaababaaabbbbbaaaaaaabbbbb",
        "aabbaaaaababaabbbbbbbbbaabaaabbb",
        "babababbababbbababbbbbababbbabbb",
        "bbbbababbababbbabababbabbabbbbbb",
        "aaaaaaaaaaaaaaaaababababbbabbbbb",
        "aabababbabbabababababababbbbabbb",
    ]) == [
        "bba",
        "bba",
        "bbba",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbbaaaaaaaa",
        "bbbbbbbbbbbbbaaaaaaa",
        "bbbbbbbbbbbbbbbb",
        "bbbbbbbbbb",
        "bbbbbbbbbbbbbbbbab",
        "bbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbabb",
        "abbbbbbbbb",
        "bbbbbbbbbbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbaaaaaaaaa",
        "bbbbbbbbbbbbbbbaaaaa",
        "bbbbbbbbbbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbbbbbbbbba",
        "bbbbbbbbbaaaaaaaaaaaaaaa",
        "bbbbbbbbbbbbbbbbba"
    ]


if __name__ == "__main__":
    test()
    main()
