import random


include = dict()
weight = dict()


def add_row(string_search, length):
    """
    :param string_search: string,
    :param length: length of string, L in problem,
    :return: score added: int,
    """
    add_score = 0
    for le in range(length - 2, length + 3):
        for i in range(20):
            st = string_search[i: i + le]
            if st in include.keys():
                if include[st] == 0:
                    add_score += weight[st]
                include[st] += 1
    return add_score


def minus_row(string_search, length):
    """
    :param string_search: string,
    :param length: length of string, L in problem,
    :return: score minus: int(positive),
    """
    minus_score = 0
    for le in range(length - 2, length + 3):
        for i in range(20):
            st = string_search[i: i + le]
            if st in include.keys():
                if include[st] == 1:
                    minus_score += weight[st]
                include[st] -= 1
    return minus_score


def make_return_from_array(s_array):
    """
    :param s_array: np.character, shape(20, 20), 2d-array for character
    :return: List[string], suitable for return
    """
    return ["".join(s_array[i]) for i in range(20)]


def solve(n, m, s_list):

    length = max([len(s) for s in s_list]) - 2

    s_array = [["A"] * 20 for _ in range(20)]
    for i in range(20):
        for j in range(20):
            s_array[i][j] = random.choice(["A", "B", "C", "D", "E", "F", "G", "H"])
    for s in s_list:
        include[s] = 0
        weight[s] = 0
    for s in s_list:
        weight[s] += 1
    score_base = 0
    for i in range(20):
        string_search = "".join(s_array[i] + s_array[i][:-1])
        score_base += add_row(string_search, length)
    for j in range(20):
        string_search = "".join([s_array[i][j] for i in range(20)] + [s_array[i][j] for i in range(19)])
        score_base += add_row(string_search, length)
    # print(score_base)

    for _ in range(30000):
        i = random.choice(range(20))
        j = random.choice(range(20))
        v = random.choice(["A", "B", "C", "D", "E", "F", "G", "H"])

        score_add = 0

        string_search = "".join(s_array[i] + s_array[i][:-1])
        score_add -= minus_row(string_search, length)
        string_search = "".join([s_array[i][j] for i in range(20)] + [s_array[i][j] for i in range(19)])
        score_add -= minus_row(string_search, length)

        v_base = s_array[i][j]
        s_array[i][j] = v

        string_search = "".join(s_array[i] + s_array[i][:-1])
        score_add += add_row(string_search, length)
        string_search = "".join([s_array[i][j] for i in range(20)] + [s_array[i][j] for i in range(19)])
        score_add += add_row(string_search, length)

        if score_add >= 0:
            score_base += score_add
        else:
            string_search = "".join(s_array[i] + s_array[i][:-1])
            _ = - minus_row(string_search, length)
            string_search = "".join([s_array[i][j] for i in range(20)] + [s_array[i][j] for i in range(19)])
            _ = - minus_row(string_search, length)

            s_array[i][j] = v_base

            string_search = "".join(s_array[i] + s_array[i][:-1])
            _ = add_row(string_search, length)
            string_search = "".join([s_array[i][j] for i in range(20)] + [s_array[i][j] for i in range(19)])
            _ = add_row(string_search, length)

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
