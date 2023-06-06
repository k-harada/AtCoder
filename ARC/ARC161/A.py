from collections import defaultdict


def solve(n, a_list):
    counter = defaultdict(int)
    for a in a_list:
        counter[a] += 1
    d = max(counter.values())
    if d <= n // 2:
        return "Yes"
    elif d == (n + 1) // 2:
        if counter[min(a_list)] == d:
            return "Yes"
        else:
            return "No"
    else:
        return "No"


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(5, [1, 2, 3, 4, 5]) == "Yes"
    assert solve(5, [1, 6, 1, 6, 1]) == "Yes"
    assert solve(5, [1, 6, 6, 6, 1]) == "No"


if __name__ == "__main__":
    test()
    main()
