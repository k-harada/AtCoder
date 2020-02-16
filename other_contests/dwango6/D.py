from heapq import heappop, heappush
from itertools import permutations


def solve(n, a_list):
    h = []
    for i in range(1, n + 1):
        heappush(h, i)
    res_list = []
    forbidden_list = []
    forbid = 0
    c1 = 0
    c2 = 0
    while len(h) > 0:
        i = heappop(h)
        if i != forbid:
            res_list.append(i)
            forbid = a_list[i - 1]
        elif len(h) > 0:
            j = heappop(h)
            res_list.append(j)
            forbid = a_list[j - 1]
            heappush(h, i)
        else:
            # print(i, res_list)
            while len(res_list) > 0:
                j = res_list.pop()
                if a_list[j - 1] == i:
                    heappush(h, j)
                else:
                    forbid = a_list[i - 1]
                    res_list.append(j)
                    res_list.append(i)
                    forbidden_list.append(i)
                    break
                c2 += 1
                if c2 > 2 * n:
                    return -1
            if len(res_list) == 0:
                # print(i, h)
                forbid = a_list[i - 1]
                res_list.append(i)
                forbidden_list.append(i)
            assert len(forbidden_list) > 0

        if len(forbidden_list) >= 2:
            if n == 2:
                return "-1"
            else:
                res_list = res_list[:n - 3]
                abc = [i for i in range(1, n + 1) if i not in res_list]
                for a, b, c in permutations(abc):
                    if len(res_list) > 0:
                        if a == a_list[res_list[-1] - 1]:
                            continue
                    if a_list[a - 1] == b:
                        continue
                    if a_list[b - 1] == c:
                        continue
                    res_list = res_list + [a, b, c]
                    h = []
                    break
                assert len(h) == 0

        c1 += 1
        if c1 > 2 * n:
            return "error"
    return " ".join([str(i) for i in res_list])


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)

    print(res)


def test():
    assert solve(4, [2, 3, 4, 1]) == "1 3 2 4"
    assert solve(2, [2, 1]) == "-1"
    assert solve(13, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12]) == "1 3 2 4 6 5 7 9 8 10 12 11 13"


if __name__ == "__main__":
    test()
    main()
