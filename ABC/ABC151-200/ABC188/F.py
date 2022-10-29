from collections import deque


def solve(x, y):
    if x >= y:
        return x - y
    res_dict = dict()
    res_dict[y] = 0
    queue = deque([y])
    while len(queue) > 0:
        p = queue.popleft()
        if p == 0:
            continue
        elif p % 2 == 0:
            q = p // 2
            if q not in res_dict.keys():
                res_dict[q] = res_dict[p] + 1
                queue.append(q)
            else:
                res_dict[q] = min(res_dict[q], res_dict[p] + 1)
            q = p // 2 - 1
            if q not in res_dict.keys():
                res_dict[q] = res_dict[p] + 2
                queue.append(q)
            else:
                res_dict[q] = min(res_dict[q], res_dict[p] + 2)
        else:
            q = p // 2
            if q not in res_dict.keys():
                res_dict[q] = res_dict[p] + 2
                queue.append(q)
            else:
                res_dict[q] = min(res_dict[q], res_dict[p] + 2)
            q = p // 2 + 1
            if q not in res_dict.keys():
                res_dict[q] = res_dict[p] + 2
                queue.append(q)
            else:
                res_dict[q] = min(res_dict[q], res_dict[p] + 2)
    # print(res_dict)
    res = abs(x - y)
    for k in res_dict.keys():
        res = min(res, abs(x - k) + res_dict[k])
    return res


def main():
    x, y = map(int, input().split())
    res = solve(x, y)
    print(res)


def test():
    assert solve(3, 9) == 3
    assert solve(7, 11) == 3
    assert solve(1000000000000000000, 1000000000000000000) == 0


if __name__ == "__main__":
    test()
    main()
