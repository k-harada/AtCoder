import math
import random
import time

include = dict()
weight = dict()


def add_row(query: int, length: int):
    """
    :param query: int, around 2 ** 60 integer to query
    :param length: length of string, L in problem,
    :return: add_score: int,
    """
    head = 1 << 60
    cut = (1 << 57) - 1
    x = query
    add_score = 0
    for i in range(20):
        for le in range(length - 2, length + 3):
            st = (head * (le - length + 3)) | (x >> (3 * (20 - le)))
            if st in include.keys():
                if include[st] == 0:
                    add_score += weight[st]
                include[st] += 1
        # roll
        x = ((x & cut) << 3) | (x >> 57)

    return add_score


def remove_row(query: int, length: int):
    """
    :param query: int, around 2 ** 60 integer to query
    :param length: length of string, L in problem,
    :return: remove_score: int(positive),
    """
    head = 1 << 60
    cut = (1 << 57) - 1
    x = query
    remove_score = 0

    for i in range(20):
        for le in range(length - 2, length + 3):
            st = (head * (le - length + 3)) | (x >> (3 * (20 - le)))
            if st in include.keys():
                if include[st] == 1:
                    remove_score += weight[st]
                include[st] -= 1
        # roll
        x = ((x & cut) << 3) + (x >> 57)
    return remove_score


def make_return_from_array(s_array):
    """
    :param s_array: np.character, shape(20, 20), 2d-array for 0-7
    :return: List[string], suitable for return
    """
    return ["".join(["ABCDEFGH"[v] for v in s_array[i]]) for i in range(20)]


def solve(n, m, s_list):

    t0 = time.time()

    length = max([len(s) for s in s_list]) - 2

    s_array = [["A"] * 20 for _ in range(20)]
    for i in range(20):
        for j in range(20):
            s_array[i][j] = random.choice(range(8))
    head = 1 << 60
    v_list = []
    for s in s_list:
        v = 0
        for c in s:
            v <<= 3
            v |= "ABCDEFGH".index(c)
        v |= (head * (len(s) - length + 3))
        v_list.append(v)
        include[v] = 0
        weight[v] = 0

    for v in v_list:
        weight[v] += 1

    score_base = 0
    for i in range(20):
        query = 0
        for j in range(20):
            query <<= 3
            query |= s_array[i][j]
        score_base += add_row(query, length)
    for j in range(20):
        query = 0
        for i in range(20):
            query <<= 3
            query |= s_array[i][j]
        score_base += add_row(query, length)
    # print(score_base)

    for it in range(1000000):
        if time.time() > t0 + 2.75:
            break
        temperature = 1000 / (it + 100)
        i0 = random.choice(range(20))
        j0 = random.choice(range(20))
        v = random.choice(range(8))

        score_add = 0
        query = 0
        for j in range(20):
            query <<= 3
            query |= s_array[i0][j]
        score_add -= remove_row(query, length)

        query = 0
        for i in range(20):
            query <<= 3
            query |= s_array[i][j0]
        score_add -= remove_row(query, length)

        v_base = s_array[i0][j0]
        s_array[i0][j0] = v

        query = 0
        for j in range(20):
            query <<= 3
            query |= s_array[i0][j]
        score_add += add_row(query, length)
        query = 0
        for i in range(20):
            query <<= 3
            query |= s_array[i][j0]
        score_add += add_row(query, length)

        if score_add >= 0 or math.exp(score_add / temperature) > random.uniform(0, 1):
            score_base += score_add
        else:
            query = 0
            for j in range(20):
                query <<= 3
                query |= s_array[i0][j]
            s_ = remove_row(query, length)

            query = 0
            for i in range(20):
                query <<= 3
                query |= s_array[i][j0]
            s_ = remove_row(query, length)

            s_array[i0][j0] = v_base

            query = 0
            for j in range(20):
                query <<= 3
                query |= s_array[i0][j]
            s_ = add_row(query, length)
            query = 0
            for i in range(20):
                query <<= 3
                query |= s_array[i][j0]
            s_ = add_row(query, length)
    # print(score_base)
    return make_return_from_array(s_array)


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
