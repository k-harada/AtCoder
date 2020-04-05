from collections import deque


def solve(n):
    if n == 1:
        return ["a"]
    alphabet = "abcdefghijkl"
    res_list = []
    queue = deque([("a", 0)])
    while len(queue) > 0:
        p, k = queue.popleft()
        for i in range(k + 2):
            q = p + alphabet[i]
            queue.append((q, max(i, k)))
            if len(q) == n:
                res_list.append(q)
        if len(q) > n:
            break
    return res_list


def main():
    n = int(input())
    res = solve(n)
    for r in res:
        print(r)


def test():
    assert solve(1) == ["a"]
    assert solve(2) == ["aa", "ab"]


if __name__ == "__main__":
    test()
    main()
