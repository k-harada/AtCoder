def find_possible(n, skill_list, d):
    r_list = [0] * 32
    for skill in skill_list:
        r = 0
        for i in range(5):
            if skill[i] >= d:
                r += 2 ** i
        r_list[r] += 1
    for i0 in range(32):
        if r_list[i0] == 0:
            continue
        for i1 in range(32):
            if r_list[i1] == 0:
                continue
            for i2 in range(32):
                if r_list[i2] == 0:
                    continue
                if (i0 | i1) | i2 == 31:
                    return True
    return False


def solve(n, skill_list):
    left = 0
    right = 10 ** 9 + 1
    while left < right - 1:
        mid = (left + right) // 2
        # print(mid)
        if find_possible(n, skill_list, mid):
            left = mid
        else:
            right = mid
    return left


def main():
    n = int(input())
    skill_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, skill_list)
    print(res)


def test():
    assert solve(3, [(3, 9, 6, 4, 6), (6, 9, 3, 1, 1), (8, 8, 9, 3, 7)]) == 4


if __name__ == "__main__":
    test()
    main()
