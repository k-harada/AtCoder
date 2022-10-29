from heapq import heappop, heappush
from bisect import bisect_left


def solve(t, n_list, lr_list_list):
    res = []
    for n, lr_list in zip(n_list, lr_list_list):

        h = []
        l_values_s = list(sorted([lr[0] for lr in lr_list]))

        right_dict = dict()
        for l, r in lr_list:
            if l not in right_dict.keys():
                right_dict[l] = []
            right_dict[l].append(r)

        left = 0
        res_now = "Yes"
        while True:
            # add balls
            if left in right_dict.keys():
                for r in right_dict[left]:
                    heappush(h, r)
            # increment left
            if len(h):
                # put ball
                r = heappop(h)
                if r < left:
                    res_now = "No"
                    break
                left += 1
            else:
                i = bisect_left(l_values_s, left + 1)
                if i == n:
                    break
                else:
                    left = l_values_s[i]

        res.append(res_now)

    # print(res)
    return res


def main():
    t = int(input())
    n_list = []
    lr_list = []
    for _ in range(t):
        n = int(input())
        lr = [tuple(map(int, input().split())) for _ in range(n)]
        n_list.append(n)
        lr_list.append(lr)
    res = solve(t, n_list, lr_list)
    for r in res:
        print(r)


def test():
    assert solve(2, [3, 5], [[(1, 2), (2, 3), (3, 3)], [(1, 2), (2, 3), (3, 3), (1, 3), (99, 100)]]) == ["Yes", "No"]


if __name__ == "__main__":
    test()
    main()
