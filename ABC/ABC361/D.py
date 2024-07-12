from collections import deque


def solve(n, s, t):
    s0 = s + ".."
    t0 = t + ".."
    dist = dict()
    dist[s0] = 0
    queue = deque([(s0, n)])
    while len(queue):
        p, np = queue.popleft()
        p_ = list(p)
        for i in range(n + 1):
            if abs(i - np) <= 1:
                continue
            q_ = p_.copy()
            q_[i] = "."
            q_[i + 1] = "."
            q_[np] = p[i]
            q_[np + 1] = p[i + 1]
            q = "".join(q_)
            if q not in dist.keys():
                dist[q] = dist[p] + 1
                queue.append((q, i))
    if t0 in dist.keys():
        return dist[t0]
    else:
        return -1


def main():
    n = int(input())
    s = input()
    t = input()
    res = solve(n, s, t)
    print(res)


def test():
    assert solve(6, "BWBWBW", "WWWBBB") == 4
    assert solve(6, "BBBBBB", "WWWWWW") == -1
    assert solve(14, "BBBWBWWWBBWWBW", "WBWWBBWWWBWBBB") == 7


if __name__ == "__main__":
    test()
    main()
