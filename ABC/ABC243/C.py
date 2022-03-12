def solve(n, xy_list, s):
    left_dict = dict()
    right_dict = dict()
    for i in range(n):
        x, y = xy_list[i]
        if s[i] == "L":
            if y not in left_dict.keys():
                left_dict[y] = x
            else:
                left_dict[y] = max(x, left_dict[y])
            if y in right_dict.keys():
                if right_dict[y] < x:
                    return "Yes"
        else:
            if y not in right_dict.keys():
                right_dict[y] = x
            else:
                right_dict[y] = min(x, right_dict[y])
            if y in left_dict.keys():
                if left_dict[y] > x:
                    return "Yes"
    return "No"


def main():
    n = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    s = input()
    res = solve(n, xy_list, s)
    print(res)


def test():
    assert solve(3, [(2, 3), (1, 1), (4, 1)], "RRL") == "Yes"
    assert solve(2, [(1, 1), (2, 1)], "RR") == "No"


if __name__ == "__main__":
    test()
    main()
