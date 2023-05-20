import math
from collections import deque


def solve(n, m):
    r = int(math.sqrt(m)) + 1
    diff = []
    for i in range(-r, r + 1):
        for j in range(-r, r + 1):
            if i ** 2 + j ** 2 == m:
                diff.append((i, j))
    # print(diff)
    queue = deque([(0, 0)])
    res = [[-1] * n for _ in range(n)]
    res[0][0] = 0
    while len(queue):
        i, j = queue.popleft()
        for d1, d2 in diff:
            p = i + d1
            q = j + d2
            if p < 0 or q < 0:
                continue
            if p >= n or q >= n:
                continue
            if res[p][q] == -1:
                res[p][q] = res[i][j] + 1
                queue.append((p, q))
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    res = solve(n, m)
    for r in res:
        print(" ".join([str(a) for a in r]))


def test():
    assert solve(3, 1) == [[0, 1, 2], [1, 2, 3], [2, 3, 4]]


if __name__ == "__main__":
    test()
    main()
