from collections import deque


def solve(s):
    r = deque()
    flag = 1
    for c in s:
        if c == "R":
            flag *= -1
        else:
            if flag == 1:
                r.append(c)
            else:
                r.appendleft(c)
    res = ""
    while r:
        c = r.popleft()
        if len(res) == 0:
            res = c
        elif c == res[-1]:
            res = res[:-1]
        else:
            res = res + c
    if flag == -1:
        res = "".join(list(reversed(res)))
    # print(res)
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("ozRnonnoe") == "zone"
    assert solve("hellospaceRhellospace") == ""


if __name__ == "__main__":
    test()
    main()
