def binary_search(cond, left_initial, right_initial):

    left = left_initial
    right = right_initial

    while left + 1 < right:
        mid = (left + right) // 2

        if cond(mid):
            right = mid
        else:
            left = mid

    return left


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


def solve_e(n, p_list):
    ind_list = [0] * (n + 1)
    for i in range(n):
        ind_list[p_list[i]] = i + 1

    bit = Bit(n + 1)

    res = 0

    for i in range(n, 0, -1):
        ind = ind_list[i]
        bit.add(ind, 1)
        # right
        r1 = n + 1
        r2 = n + 1
        if bit.sum(n + 1) - bit.sum(ind) > 0:
            r1 = binary_search(lambda k: bit.sum(k) - bit.sum(ind) >= 1, ind, n + 1) + 1
        if bit.sum(n + 1) - bit.sum(ind) > 1:
            r2 = binary_search(lambda k: bit.sum(k) - bit.sum(ind) >= 2, ind, n + 1) + 1

        # left
        l1 = 0
        l2 = 0
        if bit.sum(ind) >= 2:
            l1 = binary_search(lambda k: bit.sum(ind) - bit.sum(k) <= 1, 0, ind) + 1
        if bit.sum(ind) >= 3:
            l2 = binary_search(lambda k: bit.sum(ind) - bit.sum(k) <= 2, 0, ind) + 1
        # print(l1, l2, r1, r2, ind, i)
        cnt = (ind - l1) * (r2 - r1) + (l1 - l2) * (r1 - ind)
        res += cnt * i

    return res


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    print(solve_e(n, p_list))


if __name__ == "__main__":
    main()
