import numpy as np


def solve(n, s_list, t_list, u_list, v_list):

    x = np.zeros((n, n, 64), dtype=np.uint64)

    for k in range(64):

        # mod
        uk_list = [(u // (2 ** k)) % 2 for u in u_list]
        vk_list = [(v // (2 ** k)) % 2 for v in v_list]

        # count
        all_1_row = 0
        not_all_1_row = 0
        all_0_row = 0
        not_all_0_row = 0
        all_1_col = 0
        not_all_1_col = 0
        all_0_col = 0
        not_all_0_col = 0

        # row
        for i in range(n):
            if s_list[i] == 0 and uk_list[i] == 1:
                # all 1
                all_1_row += 1
            elif s_list[i] == 0 and uk_list[i] == 0:
                # not all 1
                not_all_1_row += 1
            elif s_list[i] == 1 and uk_list[i] == 0:
                # all 0
                all_0_row += 1
            else:
                # not all 0
                not_all_0_row += 1
        # col
        for j in range(n):
            if t_list[j] == 0 and vk_list[j] == 1:
                # all 1
                all_1_col += 1
            elif t_list[j] == 0 and vk_list[j] == 0:
                # not all 1
                not_all_1_col += 1
            elif t_list[j] == 1 and vk_list[j] == 0:
                # all 0
                all_0_col += 1
            else:
                # not all 0
                not_all_0_col += 1

        # impossible
        if all_1_row > 0 and all_0_col > 0:
            return [-1]
        elif all_0_row > 0 and all_1_col > 0:
            return [-1]
        elif all_1_col == n and not_all_1_row > 0:
            return [-1]
        elif all_0_col == n and not_all_0_row > 0:
            return [-1]
        elif all_1_row == n and not_all_1_col > 0:
            return [-1]
        elif all_0_row == n and not_all_0_col > 0:
            return [-1]

        # all 1 in both
        if all_1_row > 0 and all_1_col > 0:
            for i in range(n):
                # all 1
                if s_list[i] == 0 and uk_list[i] == 1:
                    x[i, :, k] = 1
            for j in range(n):
                # all 1
                if t_list[j] == 0 and vk_list[j] == 1:
                    x[:, j, k] = 1

        # all 0 in both
        elif all_0_row > 0 and all_0_col > 0:
            x[:, :, k] = 1
            for i in range(n):
                # all 0
                if s_list[i] == 1 and uk_list[i] == 0:
                    x[i, :, k] = 0
            for j in range(n):
                # all 0
                if t_list[j] == 1 and vk_list[j] == 0:
                    x[:, j, k] = 0

        # only row
        elif all_0_col == 0 and all_1_col == 0:
            if sum(uk_list) == n:
                x[:, :, k] = 1
                if all_1_row == n - 1:
                    if not_all_1_col == n:
                        return [-1]
                    else:
                        for i in range(n):
                            if s_list[i] == 1:
                                for j in range(n):
                                    if vk_list[j] == 0:
                                        x[i, j, k] = 0
                else:
                    cnt = 0
                    for i in range(n):
                        if s_list[i] == 1:
                            if cnt == 0:
                                x[i, 0::2, k] = 0
                            elif cnt == 1:
                                x[i, 1::2, k] = 0
                            cnt += 1

            elif sum(uk_list) == 0:
                x[:, :, k] = 0
                if all_0_row == n - 1:
                    if not_all_0_col == n:
                        return [-1]
                    else:
                        for i in range(n):
                            if s_list[i] == 0:
                                for j in range(n):
                                    if t_list[j] == 1 and vk_list[j] == 1:
                                        x[i, j, k] = 1
                else:
                    cnt = 0
                    for i in range(n):
                        if s_list[i] == 0:
                            if cnt == 0:
                                x[i, 0::2, k] = 1
                            elif cnt == 1:
                                x[i, 1::2, k] = 1
                            cnt += 1
            else:
                for i in range(n):
                    x[i, :, k] = uk_list[i]
        # only col
        else:
            if sum(vk_list) == n:
                x[:, :, k] = 1
                if all_1_col == n - 1:
                    if not_all_1_row == n:
                        return [-1]
                    else:
                        for j in range(n):
                            if t_list[j] == 1:
                                for i in range(n):
                                    if s_list[i] == 0 and uk_list[i] == 0:
                                        x[i, j, k] = 0
                else:
                    cnt = 0
                    for j in range(n):
                        if t_list[j] == 1:
                            if cnt == 0:
                                x[0::2, j, k] = 0
                            elif cnt == 1:
                                x[1::2, j, k] = 0
                            cnt += 1

            elif sum(vk_list) == 0:
                x[:, :, k] = 0
                if all_0_col == n - 1:
                    if not_all_0_row == n:
                        return [-1]
                    else:
                        for j in range(n):
                            if t_list[j] == 0:
                                for i in range(n):
                                    if s_list[i] == 1 and uk_list[i] == 1:
                                        x[i, j, k] = 1
                else:
                    cnt = 0
                    for j in range(n):
                        if t_list[j] == 0:
                            if cnt == 0:
                                x[0::2, j, k] = 1
                            elif cnt == 1:
                                x[1::2, j, k] = 1
                            cnt += 1
            else:
                for j in range(n):
                    x[:, j, k] = vk_list[j]

    for k in range(64):
        x[:, :, k] = x[:, :, k] * (2 ** k)

    y = x.sum(axis=2)
    res = []
    for i in range(n):
        res.append(" ".join([str(z) for z in y[i, :]]))

    # print(res)

    return res


def main():
    n = int(input())
    s_list = list(map(int, input().split()))
    t_list = list(map(int, input().split()))
    u_list = list(map(int, input().split()))
    v_list = list(map(int, input().split()))
    res = solve(n, s_list, t_list, u_list, v_list)
    for r in res:
        print(r)


def test():
    assert solve(2, [0, 1], [1, 0], [1, 1], [1, 0]) == 0
    assert solve(2, [1, 1], [1, 0], [15, 15], [15, 11]) == 0


if __name__ == "__main__":
    # test()
    main()
