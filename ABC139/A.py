def main():
    s = list(input())
    t = list(input())
    assert len(s) == len(t)
    res = 0
    for i, ss in enumerate(s):
        if ss == t[i]:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
