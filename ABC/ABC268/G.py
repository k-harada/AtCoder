MOD = 998244353


def solve(n, s_list):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_ind = dict()
    for i, c in enumerate(alphabet):
        alphabet_ind[c] = i
    total_len = sum([len(s) for s in s_list])
    tree = [[-1] * 26 for _ in range(total_len + 1)]
    weight = [0] * (total_len + 1)
    weight_sub = [0] * (total_len + 1)
    parent = [-1] * (total_len + 1)
    index = 0
    for s in s_list:
        current = 0
        for c in s:
            d = tree[current][alphabet_ind[c]]
            if d == -1:
                index += 1
                parent[index] = current
                tree[current][alphabet_ind[c]] = index
                current = index
            else:
                current = d
            weight_sub[current] += 1
        weight[current] += 1
    # print(parent)
    # print(weight)
    half = pow(2, MOD - 2, MOD)
    res = []
    for s in s_list:
        current = 0
        n_parents = 0
        n_children = 0
        for c in s:
            current = tree[current][alphabet_ind[c]]
            n_parents += weight[current]
        n_children = weight_sub[current]
        r = 1 + n_parents + (n - 1 - n_parents - n_children) * half
        res.append(r % MOD)
    # print(res)
    return res


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    for r in res:
        print(r)


def test():
    assert solve(3, ["a", "aa", "ab"]) == [1, 499122179, 499122179]
    assert solve(3, ["a", "aa", "aaa"]) == [1, 2, 3]


def test_large_1():
    print(solve(1, ["a" * 500000]))


if __name__ == "__main__":
    test()
    # test_large_1()
    main()
