def solve(s, t):
    assert len(s) == len(t)
    res = 0
    for i, ss in enumerate(s):
        if ss == t[i]:
            res += 1
    return res


if __name__ == "__main__":
    S = list(input())
    T = list(input())
    print(solve(S, T))
