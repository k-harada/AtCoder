import numpy as np


def solve(n, p_list):
    q_array = np.argsort(np.array(p_list))
    # print(q_array)
    return " ".join([str(q + 1) for q in q_array])


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    print(res)


def test():
    assert solve(2, [2, 3, 1]) == "3 1 2"
    assert solve(3, [1, 2, 3]) == "1 2 3"
    assert solve(5, [5, 3, 2, 4, 1]) == "5 3 2 4 1"


if __name__ == "__main__":
    test()
    main()
