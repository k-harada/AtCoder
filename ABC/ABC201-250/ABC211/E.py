from collections import deque


def solve(n, k, s):

    queue = deque()
    visited = dict()

    for i in range(n):
        for j in range(n):
            if s[i][j] == ".":
                p_int = 2 ** (i * n + j)
                visited[p_int] = 1
                queue.append((p_int, 1))

    res = 0

    while len(queue):
        p_int, p_cnt = queue.popleft()
        if p_cnt == k:
            res += 1
            # print(bin(p_int))
            continue
        for i in range(n):
            for j in range(n):
                if s[i][j] == ".":
                    if p_int & 2 ** (i * n + j):
                        continue
                    flag = 0
                    if i > 0:
                        if p_int & 2 ** ((i - 1) * n + j):
                            flag = 1
                    if i < n - 1:
                        if p_int & 2 ** ((i + 1) * n + j):
                            flag = 1
                    if j > 0:
                        if p_int & 2 ** (i * n + j - 1):
                            flag = 1
                    if j < n - 1:
                        if p_int & 2 ** (i * n + j + 1):
                            flag = 1
                    if flag == 0:
                        continue
                    q_int = p_int + 2 ** (i * n + j)
                    if q_int not in visited.keys():
                        visited[q_int] = 1
                        q_cnt = p_cnt + 1
                        queue.append((q_int, q_cnt))

    return res


def main():
    n = int(input())
    k = int(input())
    s = [list(input()) for _ in range(n)]
    res = solve(n, k, s)
    print(res)


def test():
    assert solve(3, 5, ["#.#", "...", "..#"]) == 5
    assert solve(2, 2, ["#.", ".#"]) == 0
    assert solve(8, 8, ["........." for _ in range(8)]) == 64678


if __name__ == "__main__":
    test()
    main()
