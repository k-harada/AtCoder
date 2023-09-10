from collections import deque


def solve(c):
    st = [0] * (2 ** 9)
    good = [1] * (2 ** 9)
    rule = []
    for i in range(3):
        if c[i][0] == c[i][1]:
            rule.append((i * 3, i * 3 + 1, i * 3 + 2))
        elif c[i][0] == c[i][2]:
            rule.append((i * 3, i * 3 + 2, i * 3 + 1))
        elif c[i][1] == c[i][2]:
            rule.append((i * 3 + 1, i * 3 + 2, i * 3))
    for j in range(3):
        if c[0][j] == c[1][j]:
            rule.append((j, j + 3, j + 6))
        elif c[0][j] == c[2][j]:
            rule.append((j, j + 6, j + 3))
        elif c[1][j] == c[2][j]:
            rule.append((j + 3, j + 6, j))
    if c[0][0] == c[1][1]:
        rule.append((0, 4, 8))
    elif c[0][0] == c[2][2]:
        rule.append((0, 8, 4))
    elif c[1][1] == c[2][2]:
        rule.append((4, 8, 0))
    if c[2][0] == c[1][1]:
        rule.append((6, 4, 2))
    elif c[2][0] == c[0][2]:
        rule.append((2, 6, 4))
    elif c[1][1] == c[0][2]:
        rule.append((2, 4, 6))

    for m in range(2 ** 9):
        b_list = []
        k = m
        for _ in range(9):
            b_list.append(k % 2)
            k //= 2
        for r in rule:
            if b_list[r[0]] == b_list[r[1]] == 1 and b_list[r[2]] == 0:
                good[m] = 0
    st[0] = 1
    visited = [0] * (2 ** 9)
    queue = deque([0])
    while len(queue):
        m = queue.popleft()
        if visited[m]:
            continue
        visited[m] = 1
        # print(m, st[m])
        if good[m] == 0:
            continue
        k = m
        for q in range(9):
            if k % 2 == 0:
                st[m + 2 ** q] += st[m]
                queue.append(m + 2 ** q)
            k //= 2
    res = st[-1] / (9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
    # print(res)
    return res


def main():
    c = [list(map(int, input().split())) for _ in range(3)]
    res = solve(c)
    print(res)


def test():
    assert solve([[3, 1, 9], [2, 5, 6], [2, 7, 1]]) == 2 / 3
    assert solve([[7, 7, 6], [8, 6, 8], [7, 7, 6]]) == 0.004982363315696649029982363316
    assert solve([[3, 6, 7], [1, 9, 7], [5, 7, 5]]) == 0.4


if __name__ == "__main__":
    # test()
    main()
