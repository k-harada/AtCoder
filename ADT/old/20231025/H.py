from heapq import heappop, heappush


def solve_sub(n, lr_list):
    lr_list_s = list(sorted(lr_list, key=lambda x: (x[0], x[1])))
    lr_list_s.append((10 ** 9 + 7, 10 ** 9 + 7))
    h = []
    j = 0
    t = 0
    while t <= 10 ** 9:
        if len(h) == 0:
            t = lr_list_s[j][0]

        while lr_list_s[j][0] == t:
            heappush(h, lr_list_s[j][1])
            j += 1
            if j == n + 1:
                break

        if len(h) > 0:
            k = heappop(h)
            if t > k:
                return "No"
        t += 1
    if len(h) > 0:
        return "No"
    return "Yes"


def solve(t, case_list):
    res = [solve_sub(n, lr_list) for n, lr_list in case_list]
    # print(res)
    return res


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        n = int(input())
        lr_list = [tuple(map(int, input().split())) for _ in range(n)]
        case_list.append((n, lr_list))
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(2, [(3, [(1, 2), (2, 3), (3, 3)]), (5, [(1, 2), (2, 3), (3, 3), (1, 3), (9, 10)])]) == ["Yes", "No"]


if __name__ == "__main__":
    test()
    main()
