from collections import deque


def solve(n, s):
    queue = deque()
    queue.append(n)
    for i in range(n - 1, -1, -1):
        if s[i] == "L":
            queue.append(i)
        else:
            queue.appendleft(i)
    res_list = list(queue)
    return " ".join([str(r) for r in res_list])


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(5, "LRRLR") == "1 2 4 5 3 0"
    assert solve(7, "LLLLLLL") == "7 6 5 4 3 2 1 0"


if __name__ == "__main__":
    test()
    main()
