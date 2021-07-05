def solve(h, w, n, m, ab_list, cd_list):

    res_list = [[0] * w for _ in range(h)]
    room_list = [[0] * w for _ in range(h)]

    for a, b in ab_list:
        room_list[a - 1][b - 1] = 1
    for c, d in cd_list:
        room_list[c - 1][d - 1] = -1

    # right
    for i in range(h):
        light = 0
        for j in range(w):
            if room_list[i][j] == 1:
                light = 1
            elif room_list[i][j] == -1:
                light = 0
            res_list[i][j] = max(light, res_list[i][j])
    # left
    for i in range(h):
        light = 0
        for j in range(w - 1, -1, -1):
            if room_list[i][j] == 1:
                light = 1
            elif room_list[i][j] == -1:
                light = 0
            res_list[i][j] = max(light, res_list[i][j])
    # down
    for j in range(w):
        light = 0
        for i in range(h):
            if room_list[i][j] == 1:
                light = 1
            elif room_list[i][j] == -1:
                light = 0
            res_list[i][j] = max(light, res_list[i][j])
    # up
    for j in range(w):
        light = 0
        for i in range(h - 1, -1, -1):
            if room_list[i][j] == 1:
                light = 1
            elif room_list[i][j] == -1:
                light = 0
            res_list[i][j] = max(light, res_list[i][j])

    res = 0
    for i in range(h):
        for j in range(w):
            res += res_list[i][j]

    return res


def main():
    h, w, n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    cd_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(h, w, n, m, ab_list, cd_list)
    print(res)


def test():
    assert solve(3, 3, 2, 1, [(1, 1), (2, 3)], [(2, 2)]) == 7
    assert solve(4, 4, 3, 3, [(1, 2), (1, 3), (3, 4)], [(2, 3), (2, 4), (3, 2)]) == 8
    assert solve(5, 5, 5, 1, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], [(4, 2)]) == 24


if __name__ == "__main__":
    test()
    main()
