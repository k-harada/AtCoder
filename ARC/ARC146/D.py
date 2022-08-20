from collections import deque
from heapq import heappop, heappush


def solve(n, m, k, px_qy_list):
    heap_list = [[] for _ in range(n)]
    ones = [0] * n
    for i, (p, x, q, y) in enumerate(px_qy_list):
        heappush(heap_list[p - 1], (x, q - 1, y, i))
        heappush(heap_list[q - 1], (y, p - 1, x, i))
        heappush(heap_list[p - 1], (x + 1, q - 1, y + 1, i))
        heappush(heap_list[q - 1], (y + 1, p - 1, x + 1, i))
        if x == 1:
            ones[p - 1] = 1
        if y == 1:
            ones[q - 1] = 1

    # print(heap_list)

    res = [1] * n
    queue = deque([(j, 1) for j in range(n) if ones[j] == 1])

    while len(queue):
        p, v = queue.popleft()
        if v < res[p]:
            continue
        # print(p, v, flag)
        while len(heap_list[p]):
            x, q, y, i = heappop(heap_list[p])
            if x > v:
                heappush(heap_list[p], (x, q, y, i))
                break
            else:
                if res[q] < y:
                    res[q] = y
                    queue.append((q, y))

    if max(res) <= m:
        return sum(res)
    else:
        return -1


def main():
    n, m, k = map(int, input().split())
    px_qy_list = [tuple(map(int, input().split())) for _ in range(k)]
    res = solve(n, m, k, px_qy_list)
    print(res)


def test():
    assert solve(3, 4, 3, [(3, 1, 1, 2), (1, 1, 2, 2), (3, 4, 1, 4)]) == 6
    assert solve(2, 2, 2, [(1, 1, 2, 2), (2, 1, 1, 2)]) == -1


if __name__ == "__main__":
    test()
    main()
