for_dict = {"A": "B", "B": "C", "C": "A"}
rev_dict = {"A": "C", "B": "A", "C": "B"}


def solve_sub(s, t, k):
    if t < 100:
        q, r = (k - 1) // (2 ** t), (k - 1) % (2 ** t)
    else:
        q, r = 0, k - 1
    p = s[q]
    x = 0
    while 2 ** x < r:
        x += 1
    b = (t - x) % 3
    a = (t - x) - b
    # print(p, t, a, r)
    if 2 ** (t - a) <= r:
        a = 0
    for i in range(t - a):
        if r >= 2 ** (t - a - i - 1):
            r -= 2 ** (t - a - i - 1)
            p = rev_dict[p]
        else:
            p = for_dict[p]
    return p


def solve(s, q, tk_list):
    res = [solve_sub(s, t, k) for t, k in tk_list]
    # print(res)
    return res


def main():
    s = input()
    q = int(input())
    tk_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(s, q, tk_list)
    for r in res:
        print(r)


def test():
    assert solve("ABC", 4, [(0, 1), (1, 1), (1, 3), (1, 6), (1, 5)]) == ["A", "B", "C", "B", "A"]
    assert solve("CBBAACCCCC", 5, [
        (57530144230160008, 659279164847814847),
        (29622990657296329, 861239705300265164),
        (509705228051901259, 994708708957785197),
        (176678501072691541, 655134104344481648),
        (827291290937314275, 407121144297426665),
    ]) == ["A", "A", "C", "A", "A"]


if __name__ == "__main__":
    test()
    main()
