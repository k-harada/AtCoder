from collections import deque


def solve(a, n):
    d_list = [-1] * (10 ** 6)
    d_list[1] = 0
    flag = [0] * (10 ** 6)
    queue = deque([1])
    while len(queue):
        p = queue.popleft()
        if flag[p] == 1:
            continue
        flag[p] = 1
        # op 1
        q = a * p
        if q >= 1000000:
            pass
        else:
            if d_list[q] == -1:
                d_list[q] = d_list[p] + 1
                queue.append(q)
        # op 2
        if p % 10 == 0 or p < 10:
            continue
        else:
            q = int(str(p % 10) + str(p // 10))
            if d_list[q] == -1:
                d_list[q] = d_list[p] + 1
                queue.append(q)

    return d_list[n]


def main():
    a, n = map(int, input().split())
    res = solve(a, n)
    print(res)


def test():
    assert solve(3, 72) == 4
    assert solve(2, 5) == -1
    assert solve(2, 611) == 12
    assert solve(2, 767090) == 111


if __name__ == "__main__":
    test()
    main()
