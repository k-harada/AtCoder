def solve(t, case_list):
    res = []
    for n, m, xy_list in case_list:
        s = 0
        c = 0
        r = xy_list[0][0]
        for x, y in xy_list:
            if x < 0 and c > 0:
                # 逆転の瞬間を見つける
                k = c // (-x)
                if 1 <= k <= y:
                    u = s + c * k + x * k * (k + 1) // 2
                    r = max(r, u)
                k -= 1
                if 1 <= k <= y:
                    u = s + c * k + x * k * (k + 1) // 2
                    r = max(r, u)
                k += 2
                if 1 <= k <= y:
                    u = s + c * k + x * k * (k + 1) // 2
                    r = max(r, u)

            # 端点の値を求める
            s += x * y * (y + 1) // 2 + c * y
            c += x * y

            r = max(r, s)
        res.append(r)
    return res


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        n, m = map(int, input().split())
        xy_list = [tuple(map(int, input().split())) for _ in range(n)]
        case_list.append((n, m, xy_list))
    res = solve(t, case_list)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
