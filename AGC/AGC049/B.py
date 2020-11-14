from collections import deque


def solve(n, s, t):
    queue = deque()
    keep = -1
    res = 0
    for i in range(n):
        if t[i] == '1':
            queue.append(i)
        if s[i] == '1':
            if keep != -1:
                res += i - keep
                keep = -1
            elif len(queue) > 0:
                p = queue.popleft()
                res += i - p
            else:
                keep = i
    if keep != -1 or len(queue) > 0:
        res = -1
    return res


def main():
    n = int(input())
    s = input()
    t = input()
    res = solve(n, s, t)
    print(res)


def test():
    assert solve(3, '001', '100') == 2
    assert solve(3, '001', '110') == -1
    assert solve(5, '10111', '01010') == 5


if __name__ == "__main__":
    test()
    main()
