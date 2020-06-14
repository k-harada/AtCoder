def solve(n, k, a_list):

    for t in range(k):

        left_list = [0] * n
        right_list = [0] * n

        for i in range(n):
            left = i - a_list[i] - 1
            if left >= 0:
                left_list[left] += 1
            right = i + a_list[i] + 1
            if right < n:
                right_list[right] += 1

        a_list = [n] * n

        if sum(left_list) == 0 and sum(right_list) == 0:
            break

        # right
        right_erase = 0
        for i in range(n):
            right_erase += right_list[i]
            a_list[i] -= right_erase
        # left
        left_erase = 0
        for i in range(n - 1, -1, -1):
            left_erase += left_list[i]
            a_list[i] -= left_erase

    return " ".join([str(a) for a in a_list])


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(5, 1, [1, 0, 0, 1, 0]) == "1 2 2 1 2"
    assert solve(5, 2, [1, 0, 0, 1, 0]) == "3 3 4 4 3"


if __name__ == "__main__":
    test()
    main()
