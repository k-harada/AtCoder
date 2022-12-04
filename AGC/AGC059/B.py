from collections import defaultdict


def solve_sub(n, c_list):
    counter = defaultdict(int)
    for c in c_list:
        counter[c] += 1
    ones = []
    many = []
    for c in set(c_list):
        if counter[c] == 1:
            ones.append(c)
        else:
            many.append(c)
    res = []
    if len(ones):
        res.append(ones.pop())
    for c in reversed(many):
        res.append(c)
    if len(ones):
        res.append(ones.pop())
    for c in many:
        for j in range(counter[c] - 1):
            res.append(c)
            if j < counter[c] - 2 and len(ones):
                res.append(ones.pop())
    res = res + ones
    # print(res)
    return " ".join([str(r) for r in res])


def solve(t, case_list):
    res = []
    for n, c_list in case_list:
        res.append(solve_sub(n, c_list))
    # print(res)
    return res


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        n = int(input())
        c_list = list(map(int, input().split()))
        case_list.append((n, c_list))
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [(3, [1, 2, 3]), (4, [1, 2, 1, 3]), (5, [2, 2, 5, 3, 3])]) == ["3 2 1", "3 1 2 1", "5 3 2 2 3"]


if __name__ == "__main__":
    test()
    main()
