def solve(n, s):
    s_list = list(s)
    left = 0
    right = n - 1
    for c in "abcdefghijklmnopqrstuvwxyz":
        # print(left, right)
        if left >= right:
            break
        while True:
            # left
            while s_list[left] == c and left < n:
                left += 1
                if left == n:
                    break
            if left >= right:
                break
            # right
            for r in range(right, left, -1):
                if s_list[r] == c:
                    right = r
                    break
            # print(left, right)
            if s_list[right] == c:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                right -= 1
            else:
                break
    res = "".join(s_list)
    # print(res)
    return res


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(4, "dcab") == "acdb"
    assert solve(2, "ab") == "ab"
    assert solve(16, "cabaaabbbabcbaba") == "aaaaaaabbbbcbbbc"
    assert solve(17, "snwfpfwipeusiwkzo") == "effwpnwipsusiwkzo"


if __name__ == "__main__":
    test()
    main()
