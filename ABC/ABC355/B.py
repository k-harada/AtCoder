def solve(n, m, a_list, b_list):
    ab_dict = [0] * 201
    for a in a_list:
        ab_dict[a] = 1
    for b in b_list:
        ab_dict[b] = 2
    ab_list_s = list(sorted(a_list + b_list))
    for i in range(n + m - 1):
        c, d = ab_list_s[i], ab_list_s[i + 1]
        if ab_dict[c] == ab_dict[d] == 1:
            return "Yes"
    return "No"


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, m, a_list, b_list)
    print(res)


def test():
    assert solve(3, 2, [3, 2, 5], [4, 1]) == "Yes"
    assert solve(3, 2, [3, 1, 5], [4, 2]) == "No"
    assert solve(1, 1, [1], [2]) == "No"


if __name__ == "__main__":
    test()
    main()
