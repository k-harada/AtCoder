def solve_sub(n, k, p_list, a_list):
    # count -1
    minus_count = [0] * (n + 1)
    k_count = [0] * (n + 1)
    v = [[] for _ in range(n + 1)]
    for i in range(n, 0, -1):
        a = a_list[i - 1]
        if a == -1:
            minus_count[i] += 1
        elif a == k:
            k_count[i] += 1
        elif a < k:
            v[i].append(a)
        v[i] = list(set(v[i]))
        if len(v[i]) + minus_count[i] >= k and minus_count[i] <= 1 and k_count[i] == 0:
            return "Alice"
        if i != 1:
            minus_count[p_list[i - 2]] += minus_count[i]
            k_count[p_list[i - 2]] += k_count[i]
            for x in v[i]:
                v[p_list[i - 2]].append(x)
    return "Bob"


def solve(t, case_list):
    res = [solve_sub(n, k, p_list, a_list) for n, k, p_list, a_list in case_list]
    return res


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        n, k = map(int, input().split())
        p_list = list(map(int, input().split()))
        a_list = list(map(int, input().split()))
        case_list.append((n, k, p_list, a_list))
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(2, [
        (4, 2, [1, 1, 2], [-1, -1, 3, 1]),
        (6, 4, [1, 1, 2, 1, 3], [-1, -1, -1, -1, -1, -1]),
    ]) == ["Alice", "Bob"]


if __name__ == "__main__":
    test()
    main()
