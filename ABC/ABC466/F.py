from heapq import heappop, heappush


def solve(n, x, a_list):
    m_list = [x + 1]
    for a in a_list:
        if a < m_list[-1]:
            m_list.append(a)
    h = []
    heappush(h, -(x + 1))
    counter = dict()
    counter[x + 1] = 1
    for a in m_list[1:]:
        while len(h):
            v = (-1) * heappop(h)
            if v <= a:
                heappush(h, -v)
                break
            q, r = v // a, v % a
            if a in counter.keys():
                counter[a] += q * counter[v]
            else:
                counter[a] = q * counter[v]
                heappush(h, -a)
            if r == 0:
                continue
            elif r in counter.keys():
                counter[r] += counter[v]
            else:
                counter[r] = counter[v]
                heappush(h, -r)
        # print(h)
    res = -1
    while len(h):
        v = (-1) * heappop(h)
        res += counter[v]
    # print(res)
    return res


def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        a_list = list(map(int, input().split()))
        res = solve(n, x, a_list)
        print(res)


def test():
    assert solve(3, 7, [5, 2, 3]) == 4
    assert solve(9, 31415, [9, 9, 8, 2, 4, 4, 3, 5, 3]) == 17452
    assert solve(1, 1000000000000000000, [1]) == 1000000000000000000
    assert solve(9, 20260405, [3141, 5926, 5358, 9793, 2384, 6264, 3383, 2795, 288]) == 77403


if __name__ == "__main__":
    test()
    main()
