def sub_solve(n, ab_list, base_floor, step):
    # occupied
    occupied_list = [0] * (2 * n)
    for i in range(n):
        a, b = ab_list[i]
        if base_floor <= a - 1 < base_floor + step:
            if b == -1:
                b = a + step
            else:
                if b != a + step:
                    return "No"
            if occupied_list[a - 1] or occupied_list[b - 1]:
                return "No"
            occupied_list[a - 1] = 1
            occupied_list[b - 1] = 1
        if base_floor <= b - 1 - step < base_floor + step:
            if a == -1:
                a = b - step
                if occupied_list[a - 1] or occupied_list[b - 1]:
                    return "No"
                occupied_list[a - 1] = 1
                occupied_list[b - 1] = 1
            else:
                if a != b - step:
                    return "No"

    return "Yes"


def solve(n, ab_list):
    # occupied
    occupied_list = [0] * (2 * n)
    for i in range(n):
        a, b = ab_list[i]
        if a >= b != -1:
            return "No"
        if a != -1:
            occupied_list[a - 1] += 1
        if b != -1:
            occupied_list[b - 1] += 1
    if max(occupied_list) > 1:
        return "No"
    # single
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        if dp[i] == 0:
            continue
        for j in range(1, n - i + 1):
            sub_res = sub_solve(n, ab_list, 2 * i, j)
            if sub_res == "Yes":
                dp[i + j] = 1
    if dp[n] == 1:
        return "Yes"
    else:
        return "No"


def main():
    n = int(input())
    ab_list = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(3, [[1, -1], [-1, 4], [-1, 6]]) == "Yes"
    assert solve(2, [[1, 4], [2, 3]]) == "No"
    assert solve(2, [[4, 1], [2, 4]]) == "No"


if __name__ == "__main__":
    test()
    main()
