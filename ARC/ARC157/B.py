def solve(n, k, s):
    xc = s.count("X")
    yc = s.count("Y")
    if xc == n:
        if k == 0:
            return 0
        else:
            return k - 1
    elif yc == n:
        if k == n:
            return 0
        else:
            return n - 1 - k
    if xc >= k:
        x_counts_list = []
        res = 0
        x_streak = 0
        st = "Z"
        for c in s:
            if c == "X":
                if st == "X":
                    x_streak += 1
                else:
                    st = "X"
                    x_streak = 1
            else:
                if st == "Y":
                    res += 1
                else:
                    st = "Y"
                    x_counts_list.append(x_streak)
        if st == "X":
            x_counts_list.append(x_streak)
        else:
            x_counts_list.append(0)
        # print(x_counts_list)
        m = k
        for x_count in list(sorted(x_counts_list[1:-1])):
            if x_count <= m:
                m -= x_count
                res += x_count + 1
            else:
                break
        res += m
        return res
    else:
        y_counts_list = []
        res = n - 1
        y_streak = 0
        st = "Z"
        for c in s:
            if c == "Y":
                if st == "Y":
                    y_streak += 1
                else:
                    st = "Y"
                    y_streak = 1
            else:
                if st == "X":
                    pass
                else:
                    st = "X"
                    y_counts_list.append(y_streak)
        if st == "Y":
            y_counts_list.append(y_streak)
        else:
            y_counts_list.append(0)
        # print(y_counts_list)
        m = k - xc
        if m <= y_counts_list[0] + y_counts_list[-1]:
            res -= m
            return res
        else:
            res -= y_counts_list[0] + y_counts_list[-1]
            m -= y_counts_list[0] + y_counts_list[-1]
        for y_count in list(sorted(y_counts_list[1:-1], reverse=True)):
            if y_count <= m:
                m -= y_count
                res -= y_count + 1
            else:
                break
        if m > 0:
            res -= m + 1
        return res


def main():
    n, k = map(int, input().split())
    s = input()
    res = solve(n, k, s)
    print(res)


def test():
    assert solve(5, 1, "XYXYX") == 2
    assert solve(5, 4, "XYXYX") == 2
    assert solve(5, 1, "YYXYY") == 4
    assert solve(5, 2, "XYYYY") == 3
    assert solve(5, 1, "XXXXX") == 0
    assert solve(5, 1, "YYYYY") == 3


if __name__ == "__main__":
    test()
    main()
