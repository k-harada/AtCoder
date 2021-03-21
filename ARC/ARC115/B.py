import numpy as np


def solve(n, c_list):
    if n == 1:
        return ["Yes", str(c_list[0][0]), "0"]
    c_arr = np.array(c_list)
    for i in range(1, n):
        d = c_arr[i, :] - c_arr[0, :]
        if d.min() != d.max():
            return ["No"]
    res_list = ["Yes"]
    e = c_arr[:, 0].min()
    res_list.append(" ".join([str(a - e) for a in c_arr[:, 0]]))
    res_list.append(" ".join([str(a) for a in c_arr.min(axis=0)]))
    return res_list


def main():
    n = int(input())
    c_list = [list(map(int, input().split())) for _ in range(n)]
    res_list = solve(n, c_list)
    for res in res_list:
        print(res)


def test():
    assert solve(3, [[4, 3, 5], [2, 1, 3], [3, 2, 4]]) == ["Yes", "2 0 1", "2 1 3"]
    assert solve(3, [[4, 3, 5], [2, 2, 3], [3, 2, 4]]) == ["No"]


if __name__ == "__main__":
    test()
    main()
