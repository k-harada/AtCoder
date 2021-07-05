from collections import deque


def solve(n):
    res = []
    if n % 2 == 0:
        m = n // 2
        queue = deque()
        queue.append(("", 0))
        s_list = [[] for _ in range(m + 1)]
        while len(queue):
            s, p = queue.pop()
            if len(s) == m - 1:
                if p > 0:
                    s_list[p - 1].append(s + ")")
                s_list[p + 1].append(s + "(")
            else:
                if p > 0:
                    queue.append((s + ")", p - 1))
                queue.append((s + "(", p + 1))
        t_list = [[] for _ in range(m + 1)]
        for i in range(m + 1):
            for s in s_list[i]:
                t = ""
                for c in reversed(s):
                    if c == "(":
                        t += ")"
                    else:
                        t += "("
                t_list[i].append(t)
        # print(s_list, t_list)
        for i in range(m, -1, -1):
            for s in s_list[i]:
                for t in t_list[i]:
                    res.append(s + t)
    return list(sorted(res))


def main():
    n = int(input())
    res = solve(n)
    for r in res:
        print(r)


def test():
    assert solve(2) == ["()"]
    assert solve(3) == []
    assert solve(4) == ["(())", "()()"]


if __name__ == "__main__":
    test()
    main()
