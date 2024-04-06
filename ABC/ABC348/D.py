from collections import deque


def solve(h, w, a, n, rce_list):
    st = [[-1] * w for _ in range(h)]
    energy = [[0] * w for _ in range(h)]
    si, sj, ti, tj = 0, 0, 0, 0
    for i in range(h):
        for j in range(w):
            if a[i][j] == "S":
                si, sj = i, j
            elif a[i][j] == "T":
                ti, tj = i, j
            elif a[i][j] == "#":
                energy[i][j] = -1
    for r, c, e in rce_list:
        energy[r - 1][c - 1] = e
    st[si][sj] = -1
    queue = deque([(si, sj, 0)])
    while len(queue):
        xp, yp, ep = queue.popleft()
        if energy[xp][yp] < 0:
            continue
        ep = max(ep, energy[xp][yp])
        if ep <= st[xp][yp]:
            continue
        st[xp][yp] = ep
        if (xp, yp) == (ti, tj):
            break
        if ep == 0:
            continue
        if xp > 0:
            xq, yq, eq = xp - 1, yp, ep - 1
            queue.append((xq, yq, eq))
        if xp < h - 1:
            xq, yq, eq = xp + 1, yp, ep - 1
            queue.append((xq, yq, eq))
        if yp > 0:
            xq, yq, eq = xp, yp - 1, ep - 1
            queue.append((xq, yq, eq))
        if yp < w - 1:
            xq, yq, eq = xp, yp + 1, ep - 1
            queue.append((xq, yq, eq))
    # print(st)
    if st[ti][tj] == -1:
        return "No"
    else:
        return "Yes"


def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    n = int(input())
    rce_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(h, w, a, n, rce_list)
    print(res)


def test():
    assert solve(
        4, 4, ["S...", "#..#", "#...", "..#T"],
        4, [(1, 1, 3), (1, 3, 5), (3, 2, 1), (2, 3, 1)]
    ) == "Yes"
    assert solve(2, 2, ["S.", "T."], 1, [(1, 2, 4)]) == "No"
    assert solve(
        4, 5, ["..#..", ".S##.", ".##T.", "....."],
        3, [(3, 1, 5), (1, 2, 3), (2, 2, 1)]
    ) == "Yes"


if __name__ == "__main__":
    test()
    main()
