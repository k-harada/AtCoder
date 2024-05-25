import numpy as np


def crop_np(x):
    h, w = x.shape
    hs = x.sum(axis=1)
    h_min = min([i for i in range(h) if hs[i] > 0])
    h_max = max([i for i in range(h) if hs[i] > 0])
    hw = x.sum(axis=0)
    w_min = min([j for j in range(w) if hw[j] > 0])
    w_max = max([j for j in range(w) if hw[j] > 0])
    return x[h_min:h_max+1, w_min:w_max+1]


def solve(ha, wa, a, hb, wb, b, hx, wx, x):
    a_np = np.zeros((ha, wa), dtype=int)
    for i in range(ha):
        for j in range(wa):
            if a[i][j] == "#":
                a_np[i, j] = 1
    b_np = np.zeros((hb, wb), dtype=int)
    for i in range(hb):
        for j in range(wb):
            if b[i][j] == "#":
                b_np[i, j] = 1
    x_np = np.zeros((hx, wx), dtype=int)
    for i in range(hx):
        for j in range(wx):
            if x[i][j] == "#":
                x_np[i, j] = 1
    a_np = crop_np(a_np)
    b_np = crop_np(b_np)
    x_np = crop_np(x_np)
    # print(a_np)
    # print(b_np)
    # print(x_np)

    for i in range(20):
        for j in range(20):
            r_np = np.zeros((30, 30), dtype=int)
            r_np[i:i + a_np.shape[0], j:j + a_np.shape[1]] += a_np
            r_np[10:10+b_np.shape[0], 10:10+b_np.shape[1]] += b_np
            r_np = crop_np(np.minimum(r_np, 1))
            if r_np.shape == x_np.shape:
                # print(r_np)
                # print(np.abs(r_np - x_np).sum())
                if np.abs(r_np - x_np).sum() == 0:
                    return "Yes"
    return "No"


def main():
    ha, wa = map(int, input().split())
    a = [input() for _ in range(ha)]
    hb, wb = map(int, input().split())
    b = [input() for _ in range(hb)]
    hx, wx = map(int, input().split())
    x = [input() for _ in range(hx)]
    res = solve(ha, wa, a, hb, wb, b, hx, wx, x)
    print(res)


def test():
    assert solve(
        3, 5, ["#.#..", ".....", ".#..."],
        2, 2, ["#.", ".#"],
        5, 3, ["...", "#.#", ".#.", ".#.", "..."]
    ) == "Yes"
    assert solve(
        2, 2, ["#.", ".#"],
        2, 2, ["#.", ".#"],
        2, 2, ["##", "##"],
    ) == "No"
    assert solve(1, 1, ["#"], 1, 2, ["##"], 1, 1, ["#"]) == "No"
    assert solve(
        3, 3, ["###", "...", "..."],
        3, 3, ["#..", "#..", "#.."],
        3, 3, ["..#", "..#", "###"]
    ) == "Yes"


if __name__ == "__main__":
    test()
    main()
