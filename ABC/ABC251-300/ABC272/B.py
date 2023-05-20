def solve(n, m, kx_list):
    counter = [[0] * n for _ in range(n)]
    for kx in kx_list:
        for x in kx[1:]:
            for y in kx[1:]:
                counter[x - 1][y - 1] += 1
    if min([min(counter[i]) for i in range(n)]) == 0:
        return "No"
    else:
        return "Yes"


def main():
    n, m = map(int, input().split())
    kx_list = [list(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, kx_list)
    print(res)


def test():
    assert solve(3, 3, [[2, 1, 2], [2, 2, 3], [2, 1, 3]]) == "Yes"
    assert solve(4, 2, [[3, 1, 2, 4], [3, 2, 3, 4]]) == "No"


if __name__ == "__main__":
    test()
    main()
