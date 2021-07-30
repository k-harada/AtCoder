def solve(h, w, a_array):
    sum_i = [0] * h
    sum_j = [0] * w
    for i in range(h):
        for j in range(w):
            sum_i[i] += a_array[i][j]
            sum_j[j] += a_array[i][j]
    res = []
    for i in range(h):
        res.append(" ".join(str(sum_i[i] + sum_j[j] - a_array[i][j]) for j in range(w)))
    return res


def main():
    h, w = map(int, input().split())
    a_array = [list(map(int, input().split())) for _ in range(h)]
    res = solve(h, w, a_array)
    for r in res:
        print(r)


def test():
    assert solve(3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == ["5 5 5", "5 5 5", "5 5 5"]
    assert solve(4, 4, [[3, 1, 4, 1], [5, 9, 2, 6], [5, 3, 5, 8], [9, 7, 9, 3]]) == [
        "28 28 25 26", "39 33 40 34", "38 38 36 31", "41 41 39 43"
    ]
    # print(solve(2000, 2000, [[99] * 2000 for _ in range(2000)]))


if __name__ == "__main__":
    # test()
    main()
