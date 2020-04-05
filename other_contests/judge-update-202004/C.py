from collections import deque


def solve(a1, a2, a3):
    res = 0
    queue = deque([[[1], [], [], 1]])
    while len(queue) > 0:
        p1, p2, p3, mp = queue.popleft()
        if mp == a1 + a2 + a3:
            res += 1
            continue
        if len(p1) < a1:
            new_p = [p1 + [mp + 1], p2, p3, mp + 1]
            queue.append(new_p)
        if len(p2) < a2 and len(p2) < len(p1):
            new_p = [p1, p2 + [mp + 1], p3, mp + 1]
            queue.append(new_p)
        if len(p3) < a3 and len(p3) < len(p2):
            new_p = [p1, p2, p3 + [mp + 1], mp + 1]
            queue.append(new_p)

    return res


def main():
    a1, a2, a3 = map(int, input().split())
    res = solve(a1, a2, a3)
    print(res)


def test():
    assert solve(1, 1, 1) == 1
    assert solve(2, 1, 1) == 3
    assert solve(2, 2, 1) == 5


if __name__ == "__main__":
    test()
    main()
