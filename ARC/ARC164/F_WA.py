from heapq import heappop, heappush


def solve(n, p_list):
    parents = [0] * n
    depth = [0] * n
    children = [0] * n
    for i, p in enumerate(p_list):
        parents[i + 1] = p - 1
        depth[i + 1] = depth[p - 1] + 1
        children[p - 1] += 1
    h = []
    res = 0
    for i in range(n):
        if children[i] == 0:
            heappush(h, (depth[i] % 2, i))
    t = 0
    dislikes = []
    while t < n:
        if len(h):
            d, i = heappop(h)
            p = parents[i]
            if d == 0:
                # print(t, i)
                if t % 2 == 0:
                    res += 1
                children[p] -= 1
                if children[p] == 0:
                    heappush(h, (depth[p] % 2, p))
                t += 1
            elif children[p] > 1:
                # print(t, i)
                if t % 2 == 1:
                    res += 1
                children[p] -= 1
                t += 1
            else:
                dislikes.append(i)
        else:
            i = dislikes.pop()
            p = parents[i]
            children[p] -= 1
            heappush(h, (depth[p] % 2, p))
            # print(t, i)
            if t % 2 == 1:
                res += 1
            t += 1
    # print(res)
    return res


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    print(res)


def test():
    assert solve(4, [1, 1, 2]) == 2
    assert solve(7, [1, 1, 2, 4, 4, 4]) == 5


if __name__ == "__main__":
    test()
    main()
