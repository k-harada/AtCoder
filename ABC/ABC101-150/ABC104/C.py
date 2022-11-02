def solve(d, g, pc_list):
    res = 1000
    # コンプリートボーナスを得るパターンを全探索
    for i in range(2 ** d):
        r = 0
        s = 0
        non_solved_max = 0
        for j in range(d):
            if (i // (2 ** j)) % 2 == 1:
                r += pc_list[j][0]
                s += pc_list[j][1] + (j + 1) * 100 * pc_list[j][0]
            else:
                non_solved_max = max(non_solved_max, j)
        if s < g:
            a = g - s
            p = (non_solved_max + 1) * 100
            r_add = (a + (-a) % p) // p
            if r_add < pc_list[non_solved_max][0]:
                r += r_add
            else:
                r = 1000
        res = min(r, res)
        # print(i, res)
    return res


def main():
    d, g = map(int, input().split())
    pc_list = [tuple(map(int, input().split())) for _ in range(d)]
    res = solve(d, g, pc_list)
    print(res)


def test():
    assert solve(2, 700, [(3, 500), (5, 800)]) == 3
    assert solve(2, 2000, [(3, 500), (5, 800)]) == 7
    assert solve(2, 400, [(3, 500), (5, 800)]) == 2
    assert solve(5, 25000, [(20, 1000), (40, 1000), (50, 1000), (30, 1000), (1, 1000)]) == 66


if __name__ == "__main__":
    test()
    main()
