def solve(n, a_list):
    res = 0
    for i in range(n - 1, 0, -1):
        res += i * ((n + 1 - i) // 2)
    a_set = list(sorted(list(set(a_list))))
    m = len(a_set)
    v_dict = dict()
    for i, a in enumerate(a_set):
        v_dict[a] = i
    positions_list = [[] for _ in range(m)]
    for i, a in enumerate(a_list):
        positions_list[v_dict[a]].append(i)

    # print(positions)

    for i in range(m):
        positions = positions_list[i]
        if len(positions) == 1:
            continue
        left = 0
        right = len(positions) - 1

        while left < right:
            left_count = positions[left] + 1
            right_count = n - positions[right]
            if left_count < right_count:
                res -= left_count * (right - left)
                left += 1
            else:
                res -= right_count * (right - left)
                right -= 1

    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(5, [5, 2, 1, 2, 2]) == 9


if __name__ == "__main__":
    test()
    main()
