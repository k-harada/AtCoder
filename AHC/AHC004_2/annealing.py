import numpy as np
import numba


@numba.njit('i8(i8[:, :], i8, i8[:], i8[:], i8[:], i8[:], i8[:])')
def judge(s_array, length, ans_array_1, ans_array_2, ans_array_3, ans_array_4, ans_array_5):
    """
    :param s_array: np.int64, shape(40, 20), 2d-array for assignment
    :param length: int64, base length for string(L in the problem)
    :param ans_array_1: np.int64, 1d-array for answer (from s_list), with length L - 2
    :param ans_array_2: np.int64, 1d-array for answer (from s_list), with length L - 1
    :param ans_array_3: np.int64, 1d-array for answer (from s_list), with length L
    :param ans_array_4: np.int64, 1d-array for answer (from s_list), with length L + 1
    :param ans_array_5: np.int64, 1d-array for answer (from s_list), with length L + 2
    :return: score
    """
    t_array = np.zeros((40, 20), dtype=np.int64)
    for i in range(40):
        r = np.int64(0)
        for j in range(20):
            r <<= 3
            r += s_array[i, j]
        for j in range(20):
            t_array[i, j] = r
            r &= (2 ** 57 - 1)
            r <<= 3
            r += s_array[i, j]

    score = np.int64(0)

    # ans_array_5
    y = np.sort((t_array >> (18 - length) * 3).reshape((800, )))
    x = ans_array_5
    i = 0
    j = 0
    while i < x.shape[0] and j < y.shape[0]:
        if x[i] < y[j]:
            i += 1
        elif x[i] == y[j]:
            score += 1
            i += 1
        else:
            j += 1

    # ans_array_4
    y >>= 3
    x = ans_array_4
    i = 0
    j = 0
    while i < x.shape[0] and j < y.shape[0]:
        if x[i] < y[j]:
            i += 1
        elif x[i] == y[j]:
            score += 1
            i += 1
        else:
            j += 1

    # ans_array_3
    y >>= 3
    x = ans_array_3
    i = 0
    j = 0
    while i < x.shape[0] and j < y.shape[0]:
        if x[i] < y[j]:
            i += 1
        elif x[i] == y[j]:
            score += 1
            i += 1
        else:
            j += 1

    # ans_array_2
    y >>= 3
    x = ans_array_2
    i = 0
    j = 0
    while i < x.shape[0] and j < y.shape[0]:
        if x[i] < y[j]:
            i += 1
        elif x[i] == y[j]:
            score += 1
            i += 1
        else:
            j += 1

    # ans_array_1
    y >>= 3
    x = ans_array_1
    i = 0
    j = 0
    while i < x.shape[0] and j < y.shape[0]:
        if x[i] < y[j]:
            i += 1
        elif x[i] == y[j]:
            score += 1
            i += 1
        else:
            j += 1

    return score


def make_return_from_array(u_array):
    """
    :param u_array: np.int64, shape(20, 20), 2d-array for assignment
    :return: List[string], suitable for return
    """
    return ["".join(["ABCDEFGH"[v] for v in u_array[i, :]]) for i in range(20)]


def solve(n, m, s_list):

    # prepare
    length = max([len(s) for s in s_list]) - 2

    ans_list = [[] for _ in range(5)]

    for s in s_list:
        x = 0
        for c in s:
            x *= 8
            x += "ABCDEFGH".index(c)
        ans_list[len(s) + 2 - length].append(x)

    ans_array_1 = np.array(ans_list[0]).astype(np.int64)
    ans_array_2 = np.array(ans_list[1]).astype(np.int64)
    ans_array_3 = np.array(ans_list[2]).astype(np.int64)
    ans_array_4 = np.array(ans_list[3]).astype(np.int64)
    ans_array_5 = np.array(ans_list[4]).astype(np.int64)

    s_array = np.random.choice(8, size=(40, 20)).astype(np.int64)

    score_base = judge(s_array, length, ans_array_1, ans_array_2, ans_array_3, ans_array_4, ans_array_5)
    print(score_base)

    for _ in range(30000):
        i, j = np.random.choice(20, size=2)
        v = np.random.choice(8)
        v_base = s_array[i, j]
        s_array[i, j] = v
        score_new = judge(s_array, length, ans_array_1, ans_array_2, ans_array_3, ans_array_4, ans_array_5)
        if score_new >= score_base:
            score_base = score_new
            pass
        else:
            s_array[i, j] = v_base
    print(score_base)
    return make_return_from_array(s_array[:20, :])


def main():
    n, m = map(int, input().split())
    s_list = [input() for _ in range(m)]
    res_list = solve(n, m, s_list)
    for res in res_list:
        print(res)


def test():
    print(solve(20, 5, ["A", "ABC", "ABDCKUHMMDSSAHHGJJF", "ABD", "ERABDCKUHMMDSSAHHGJ"]))


if __name__ == "__main__":
    # test()
    main()
