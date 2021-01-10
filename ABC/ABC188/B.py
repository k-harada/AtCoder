import numpy as np


def solve(n, a_list, b_list):
    x = np.dot(np.array(a_list), np.array(b_list))
    # print(x)
    if x == 0:
        return 'Yes'
    else:
        return 'No'


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    print(res)


def test():
    assert solve(2, [-3, 6], [4, 2]) == 'Yes'
    assert solve(2, [4, 5], [-1, -3]) == 'No'
    assert solve(3, [1, 3, 5], [3, -6, 3]) == 'Yes'


if __name__ == "__main__":
    test()
    main()
