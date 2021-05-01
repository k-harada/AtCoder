from collections import deque


def solve(n, m, a_list):
    k = n.bit_length() - 1
    basis = []
    rank = []
    ok_list = [True] * (n + 1)
    for a in a_list:
        ok_list[a] = False

    for i in range(1, n):
        if not ok_list[i]:
            continue
        a = i
        for b in basis:
            a = min(a, a ^ b)
        if a:
            basis.append(a)
            basis = list(sorted(basis, reverse=True))
            rank.append(i)

    if len(rank) < k:
        return [-1]

    res_list = []
    in_list = [0] * n
    in_list[0] = 1
    queue = deque([0])
    while len(queue):
        p = queue.popleft()
        for b in rank:
            q = p ^ b
            if in_list[q] == 0:
                in_list[q] = 1
                res_list.append(f'{p} {q}')
                queue.append(q)
    # print(res_list)
    # assert len(res_list) == n - 1
    return res_list


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res_list = solve(n, m, a_list)
    for res in res_list:
        print(res)


def test():
    assert solve(4, 1, [3]) == ["0 1", "0 2", "1 3"]
    assert solve(8, 0, []) == ['0 1', '0 2', '0 4', '1 3', '1 5', '2 6', '3 7']
    assert solve(8, 7, [1, 2, 3, 4, 5, 6, 7]) == [-1]


if __name__ == "__main__":
    test()
    main()
