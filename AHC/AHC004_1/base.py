import numpy as np
import numba


@numba.jit('i4[:](i4[:])')
def partial_match_array(word):
    table = np.zeros(word.shape[0] + 1, dtype=np.int32)
    table[0] = -1
    i, j = 0, 1

    while j < word.shape[0]:
        matched = (word[i] == word[j])

        if not matched and i > 0:
            i = table[i]
        else:
            if matched:
                i += 1
            j += 1
            table[j] = i

    return table


@numba.jit('i4(i4[:], i4[:])')
def kmp_search_duplicate(string, pattern):
    table = partial_match_array(pattern)
    i = j = 0
    while i < string.shape[0] and j < pattern.shape[0]:
        if string[i] == pattern[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = table[j]

    return j


@numba.njit('Tuple((i4, i4))(i4[:], i4[:])')
def bind(a, b):
    # a -> b
    ind_a = kmp_search_duplicate(a, b)

    # b -> a
    ind_b = kmp_search_duplicate(b, a)

    return ind_a, ind_b


@numba.njit('i4[:, :](i4[:, :], i4, i4, i4)')
def bind_array(res, bar, m, debug):
    cnt = 0
    # bind
    length_array = [0] * m
    for i in range(m):
        for j in range(20):
            if res[i, j] == 0:
                length_array[i] = j
                break
    for i in range(m):
        if length_array[i] == 0:
            continue
        for j in range(m):
            if i == j:
                continue
            ind_a, ind_b = bind(res[i, :length_array[i]], res[j, :length_array[j]])
            len_i = length_array[i]
            len_j = length_array[j]
            if len_j == 0:
                continue
            # if length_array[i] + length_array[j] - ind_a - ind_b == 20:
            #     if debug == 1:
            #         print(res[i, :len_i], res[j, :len_j])
            #     # new loop
            #     for k in range(20 - len_i):
            #         res[i, len_i + k] = res[j, ind_a + k]
            #     for k in range(20):
            #         res[j, k] = 0
            #     length_array[i] = 20
            #     length_array[j] = 0
            #     cnt += 1
            #     if debug == 1:
            #         print(res[i, :length_array[i]])
            if ind_a >= ind_b:
                if len_i + len_j - ind_a <= 20:
                    if ind_a > bar or ind_a == min(len_i, len_j):
                        if debug == 1:
                            print(res[i, :len_i], res[j, :len_j])
                        for k in range(len_j - ind_a):
                            res[i, len_i + k] = res[j, ind_a + k]
                        for k in range(20):
                            res[j, k] = 0
                        length_array[i] = length_array[i] + length_array[j] - ind_a
                        length_array[j] = 0
                        cnt += 1
                        if debug == 1:
                            print(res[i, :length_array[i]])
            else:
                if len_i + len_j - ind_b <= 20:
                    if ind_b > bar or ind_b == min(len_i, len_j):
                        if debug == 1:
                            print(res[i, :len_i], res[j, :len_j])
                        for k in range(len_i - ind_b):
                            res[j, len_j + k] = res[i, ind_b + k]
                        for k in range(20):
                            res[i, k] = res[j, k]
                            res[j, k] = 0
                        length_array[i] = length_array[i] + length_array[j] - ind_b
                        length_array[j] = 0
                        cnt += 1
                        if debug == 1:
                            print(res[i, :length_array[i]])
    # print(cnt)
    return res


@numba.njit('Tuple((i4[:, :], i4))(i4[:, :], i4[:], i4)')
def auto_fill(res, x, bar):
    max_score = -1
    max_i = 0
    max_j = 0
    flag = 0
    for i in range(20):
        for j in range(20):
            score = 0
            for k, v in enumerate(x):
                if res[i, (j + k) % 20] == v:
                    score += 1
                elif res[i, (j + k) % 20] == 0:
                    pass
                else:
                    score -= 10000
            # print(i, j, score)
            if score > max_score:
                max_score = score
                max_i = i
                max_j = j
                flag = 1

    for i in range(20):
        for j in range(20):
            score = 0
            for k, v in enumerate(x):
                if res[(i + k) % 20, j] == v:
                    score += 1
                elif res[(i + k) % 20, j] == 0:
                    pass
                else:
                    score -= 10000
            # print(i, j, score)
            if score > max_score:
                max_score = score
                max_i = i
                max_j = j
                flag = -1
    # print(max_i, max_j, flag, max_score)
    if max_score >= bar:
        if flag == 1:
            for k, v in enumerate(x):
                res[max_i, (max_j + k) % 20] = v
        else:
            for k, v in enumerate(x):
                res[(max_i + k) % 20, max_j] = v

    return res, max_score


def solve(n, m, s_list):
    # input
    res = np.zeros((m, 20), dtype=np.int32)
    for i, s in enumerate(s_list):
        for j, c in enumerate(s):
            res[i, j] = ".ABCDEFGH".index(c)
    res = bind_array(res, 100, m, 0)
    res = bind_array(res, 100, m, 0)
    res = bind_array(res, 10, m, 0)
    res = bind_array(res, 10, m, 0)
    res = bind_array(res, 9, m, 0)
    res = bind_array(res, 9, m, 0)
    res = bind_array(res, 8, m, 0)
    res = bind_array(res, 8, m, 0)
    res = bind_array(res, 7, m, 0)
    res = bind_array(res, 7, m, 0)
    res = bind_array(res, 6, m, 0)
    res = bind_array(res, 6, m, 0)
    res = bind_array(res, 5, m, 0)
    res = bind_array(res, 5, m, 0)
    res = bind_array(res, 4, m, 0)
    res = bind_array(res, 4, m, 0)
    # print((res[:, 0] != 0).sum())

    # greedy
    length_array = np.int32(20) * np.ones(m, dtype=np.int32)
    for i in range(m):
        for j in range(20):
            if res[i, j] == 0:
                length_array[i] = j
                break

    args_0 = np.argsort(-length_array)
    print([length_array[a] for a in args_0[:100]])
    for a in args_0[:100]:
        print(res[a, :])

    score_put_max = 0
    res_str = ["." * 20 for _ in range(20)]
    for _ in range(30):
        score_put = 0
        res_2 = np.zeros((20, 20), dtype=np.int32)
        length_array_noise = length_array + 0.5 * np.random.uniform(size=m)
        args = np.argsort(-length_array_noise)

        for a in args:
            if a == args[0]:
                res_2[0, :] = res[a]
                continue
            res_2, score = auto_fill(res_2, res[a, :length_array[a]], 1)
            if score > 0:
                score_put += 1
            # print(score, res[a, :length_array[a]])
            #    print(res_2)
        # print(score_put)
        if score_put > score_put_max:
            score_put_max = score_put
            # convert
            res_str = ["".join([".ABCDEFGH"[v] for v in res_2[i, :]]) for i in range(20)]

    return res_str


def main():
    n, m = map(int, input().split())
    s_list = [input() for _ in range(m)]
    res_list = solve(n, m, s_list)
    for res in res_list:
        print(res)


if __name__ == "__main__":
    main()