import random


def judge_row(string_search, m, s_list):
    """
    :param string_search: string
    :param m: int
    :param s_list: List[string]
    :return: score_array: np.int,
    """
    score_array = [0] * len(s_list)
    for i, s in enumerate(s_list):
        if s in string_search:
            score_array[i] = 1
    return score_array


def make_return_from_array(s_array):
    """
    :param s_array: np.character, shape(20, 20), 2d-array for character
    :return: List[string], suitable for return
    """
    return ["".join(s_array[i]) for i in range(20)]


def solve(n, m, s_list):

    s_array = [["A"] * 20 for _ in range(40)]
    for i in range(40):
        for j in range(20):
            s_array[i][j] = random.choice(["A", "B", "C", "D", "E", "F", "G", "H"])
    include = [[0] * m for _ in range(40)]
    for i in range(40):
        string_search = "".join(s_array[i] + s_array[i][:-1])
        include[i] = judge_row(string_search, m, s_list)

    score_base = sum([max([include[i][j] for i in range(40)]) for j in range(m)])
    print(score_base)

    for _ in range(30000):
        i = random.choice(range(40))
        j = random.choice(range(20))
        v = random.choice(["A", "B", "C", "D", "E", "F", "G", "H"])
        v_base = s_array[i][j]
        s_array[i][j] = v
        string_search = "".join(s_array[i] + s_array[i][:-1])
        include[i] = judge_row(string_search, m, s_list)
        score_new = sum([max([include[i][j] for i in range(40)]) for j in range(m)])
        if score_new >= score_base:
            score_base = score_new
            pass
        else:
            s_array[i][j] = v_base
            string_search = "".join(s_array[i] + s_array[i][:-1])
            include[i] = judge_row(string_search, m, s_list)
    print(score_base)
    return make_return_from_array(s_array[:20])


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
