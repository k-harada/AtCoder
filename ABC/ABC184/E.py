from collections import deque


def solve(h, w, a):
    points_dict = dict()
    for s in 'abcdefghijklmnopqrstuvwxyzSG':
        points_dict[s] = []

    # find characters
    for i in range(h):
        for j in range(w):
            if a[i][j] != "." and a[i][j] != "#":
                points_dict[a[i][j]].append((i, j))

    distance = [[-1] * w for _ in range(h)]
    visited_abc = dict()
    for s in 'abcdefghijklmnopqrstuvwxyz':
        visited_abc[s] = 0
    i0, j0 = points_dict['S'][0]
    distance[i0][j0] = 0

    queue = deque([(i0, j0)])
    while len(queue) > 0:
        p, q = queue.popleft()
        d = distance[p][q] + 1
        if p > 0:
            s, t = p - 1, q
            if distance[s][t] == -1:
                if a[s][t] == 'G':
                    return d
                if a[s][t] != '#':
                    distance[s][t] = d
                    queue.append((s, t))
        if q > 0:
            s, t = p, q - 1
            if distance[s][t] == -1:
                if a[s][t] == 'G':
                    return d
                if a[s][t] != '#':
                    distance[s][t] = d
                    queue.append((s, t))
        if p < h - 1:
            s, t = p + 1, q
            if distance[s][t] == -1:
                if a[s][t] == 'G':
                    return d
                if a[s][t] != '#':
                    distance[s][t] = d
                    queue.append((s, t))
        if q < w - 1:
            s, t = p, q + 1
            if distance[s][t] == -1:
                if a[s][t] == 'G':
                    return d
                if a[s][t] != '#':
                    distance[s][t] = d
                    queue.append((s, t))
        if a[p][q] in 'abcdefghijklmnopqrstuvwxyz' and visited_abc[a[p][q]] == 0:
            visited_abc[a[p][q]] = 1
            for s, t in points_dict[a[p][q]]:
                if distance[s][t] == -1:
                    if a[s][t] == 'G':
                        return d
                    if a[s][t] != '#':
                        distance[s][t] = d
                        queue.append((s, t))
    return -1


def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    res = solve(h, w, a)
    print(res)


def test():
    assert solve(2, 5, ['S.b.b', 'a.a.G']) == 4


if __name__ == "__main__":
    test()
    main()
