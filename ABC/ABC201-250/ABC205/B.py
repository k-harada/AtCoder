def solve(n, a_list):
    count_list = [0] * (n + 1)
    for a in a_list:
        count_list[a] += 1
    if max(count_list) > 1:
        return 'No'
    else:
        return 'Yes'


def main():
    n = int(input())
    a_list = map(int, input().split())
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(5, [3, 1, 2, 4, 5]) == 'Yes'
    assert solve(6, [3, 1, 4, 1, 5, 2]) == 'No'
    assert solve(3, [1, 2, 3]) == 'Yes'
    assert solve(1, [1]) == 'Yes'


if __name__ == "__main__":
    test()
    main()
