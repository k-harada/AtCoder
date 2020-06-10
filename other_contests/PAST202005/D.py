import numpy as np

BASE_ARR = np.array([
    list('.###..#..###.###.#.#.###.###.###.###.###.'),
    list('.#.#.##....#...#.#.#.#...#.....#.#.#.#.#.'),
    list('.#.#..#..###.###.###.###.###...#.###.###.'),
    list('.#.#..#..#.....#...#...#.#.#...#.#.#...#.'),
    list('.###.###.###.###...#.###.###...#.###.###.')
])


def key_match(s_sub_arr):
    for k in range(10):
        if (s_sub_arr == BASE_ARR[:, 4 * k + 1:4 * k + 4]).min():
            return k
    raise ValueError


def solve(n, s_arr):
    res_list = []
    for i in range(n):
        k = key_match(s_arr[:, 4 * i + 1:4 * i + 4])
        res_list.append(str(k))
    return "".join(res_list)


def main():
    n = int(input())
    s_arr = np.array([list(input()) for _ in range(5)])
    res = solve(n, s_arr)
    print(res)


if __name__ == "__main__":
    main()
