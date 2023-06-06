def solve(n, sa_list):
    min_i = 0
    min_a = 10 ** 9 + 7
    for i, (_, a) in enumerate(sa_list):
        if a < min_a:
            min_i = i
            min_a = a
    return [s for s, a in sa_list[min_i:] + sa_list[:min_i]]


def main():
    n = int(input())
    sa_list = []
    for _ in range(n):
        s, a_ = input().split()
        sa_list.append((s, int(a_)))
    res = solve(n, sa_list)

    # print(res)
    for r in res:
        print(r)


def test():
    assert solve(5, [
        ("alice", 31),
        ("bob", 41),
        ("carol", 5),
        ("dave", 92),
        ("ellen", 65),
    ]) == ["carol", "dave", "ellen", "alice", "bob"]
    assert solve(2, [("takahashi", 1000000000), ("aoki", 999999999)]) == ["aoki", "takahashi"]


if __name__ == "__main__":
    test()
    main()
