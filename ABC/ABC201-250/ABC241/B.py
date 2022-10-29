def solve(n, m, a_list, b_list):

    pasta_dict = dict()
    for a in a_list:
        if a not in pasta_dict.keys():
            pasta_dict[a] = 1
        else:
            pasta_dict[a] += 1

    for b in b_list:
        if b not in pasta_dict.keys():
            return "No"
        elif pasta_dict[b] == 0:
            return "No"
        else:
            pasta_dict[b] -= 1

    return "Yes"


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, m, a_list, b_list)
    print(res)


def test():
    assert solve(3, 2, [1, 1, 3], [3, 1]) == "Yes"
    assert solve(1, 1, [1000000000], [1]) == "No"
    assert solve(5, 2, [1, 2, 3, 4, 5], [5, 5]) == "No"


if __name__ == "__main__":
    test()
    main()
