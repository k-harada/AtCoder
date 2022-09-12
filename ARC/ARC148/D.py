from collections import defaultdict


def solve(n, m, a_list):
    count_dict = defaultdict(int)
    for a in a_list:
        count_dict[a] += 1

    if m % 2 == 1:
        for a in count_dict.keys():
            if count_dict[a] % 2 == 1:
                return "Alice"
    else:
        d = m // 2
        c = 0
        for a in count_dict.keys():
            if count_dict[a] % 2 == 1:
                if count_dict[(a + d) % m] % 2 == 1:
                    c += 1
                else:
                    return "Alice"
        if c % 4 != 0:
            return "Alice"
    return "Bob"


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(2, 9, [1, 4, 8, 5]) == "Alice"
    assert solve(3, 998244353, [1, 2, 3, 1, 2, 3]) == "Bob"


if __name__ == "__main__":
    test()
    main()
