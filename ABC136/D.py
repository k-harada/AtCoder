submit = True


def solve_d(test=False, s="RL"):

    if not test:
        s = input()
    res_list = [0] * len(s)

    LR_list = [-1]
    RL_list = []

    for i in range(len(s) - 1):
        if s[i] == "R" and s[i + 1] == "L":
            RL_list.append(i)
        elif s[i] == "L" and s[i + 1] == "R":
            LR_list.append(i)
    LR_list.append(len(s) - 1)
    # print(LR_list)
    # print(RL_list)
    for j in range(len(RL_list)):
        r_cnt = RL_list[j] - LR_list[j]
        l_cnt = LR_list[j + 1] - RL_list[j]
        # print(r_cnt, l_cnt)
        res_list[RL_list[j]] += r_cnt - (r_cnt // 2)
        res_list[RL_list[j] + 1] += r_cnt // 2
        res_list[RL_list[j] + 1] += l_cnt - (l_cnt // 2)
        res_list[RL_list[j]] += l_cnt // 2

    print(" ".join([str(res_list[i]) for i in range(len(s))]))


if __name__ == "__main__":
    if submit:
        solve_d()
    else:
        solve_d(test=True, s="RRLRL")
        solve_d(test=True, s="RRLLLLRLRRLL")
        solve_d(test=True, s="RRRLLRLLRRRLLLLL")
