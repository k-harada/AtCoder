from heapq import heappop, heappush


def solve(n, m, k, uv_list, a_list, b_list):
    g = [[] for _ in range(n + 1)]
    for u, v in uv_list:
        g[u].append(v)
        g[v].append(u)
    d = [k + 1] * (n + 1)
    if a_list[0] == b_list[0]:
        d[1] = 1
    else:
        d[1] = 0
    queue = []
    heappush(queue, (d[1], 1))
    while len(queue):
        v, p = heappop(queue)
        if d[p] < v:
            continue
        for q in g[p]:
            if v < k:
                if a_list[q - 1] == b_list[v]:
                    if d[q] > v + 1:
                        d[q] = v + 1
                        heappush(queue, (d[q], q))
                else:
                    if d[q] > v:
                        d[q] = v
                        heappush(queue, (d[q], q))
            else:
                if d[q] > v:
                    d[q] = v
                    heappush(queue, (d[q], q))
    # print(d)
    if d[n] == k:
        return "Yes"
    else:
        return "No"


def main():
    n, m, k = map(int, input().split())
    uv_list = [tuple(map(int, input().split())) for _ in range(m)]
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, m, k, uv_list, a_list, b_list)
    print(res)


if __name__ == "__main__":
    main()
