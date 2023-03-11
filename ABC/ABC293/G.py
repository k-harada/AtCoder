import math


def solve(n, q, a_list, lr_list):
    m = max(a_list)
    adds = [0] * (n + 1)
    for i in range(3, n + 1):
        adds[i] = (i * (i - 1) * (i - 2)) // 6
    # print(adds)
    # mo's algorithm
    sort_list = []
    for i, (l, r) in enumerate(lr_list):
        d = int(math.sqrt(l))
        sort_list.append((l - 1, r - 1, d, i))
    sort_list = sorted(sort_list, key=lambda x: (x[2], x[1]))
    # print(sort_list)
    counter = [0] * (m + 1)
    for a in a_list:
        counter[a] += 1
    adds_list = [0] * (m + 1)
    for i in range(m + 1):
        adds_list[i] = adds[counter[i]]
    res = sum(adds_list)
    left = 0
    right = n - 1
    res_list = [0] * q
    # print(counter)
    for l, r, _, i in sort_list:
        # print(l, r, left, right)
        while left < l:
            a = a_list[left]
            counter[a] -= 1
            res -= adds[counter[a] + 1] - adds[counter[a]]
            left += 1
        while left > l:
            a = a_list[left - 1]
            counter[a] += 1
            res += adds[counter[a]] - adds[counter[a] - 1]
            left -= 1
        while right > r:
            a = a_list[right]
            counter[a] -= 1
            res -= adds[counter[a] + 1] - adds[counter[a]]
            right -= 1
        while right < r:
            a = a_list[right + 1]
            counter[a] += 1
            res += adds[counter[a]] - adds[counter[a] - 1]
            right += 1
        res_list[i] = res
        # print(counter)
        # print(res)
    # print(res_list)
    return res_list


def main():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    lr_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, a_list, lr_list)
    for r in res:
        print(r)


def test():
    assert solve(10, 4, [2, 7, 1, 8, 2, 8, 1, 8, 2, 8], [(1, 10), (1, 9), (2, 10), (5, 5)]) == [5, 2, 4, 0]


if __name__ == "__main__":
    test()
    main()
