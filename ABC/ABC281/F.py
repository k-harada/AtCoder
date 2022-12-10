def solve(n, a_list):
    a_list_s = list(sorted(a_list))
    left = [0] * n
    max_v = [a for a in a_list_s]
    for i in range(29, -1, -1):
        s = 0
        while s < n:
            t = s
            for t in range(s, n + 1):
                if t == n:
                    break
                if left[t] != left[s]:
                    break
            r = 0
            for j in range(s, t):
                # 区間に0と1が両方あるか数える
                d = (a_list_s[j] >> i) & 1
                r |= 2 ** d
            if r == 3:
                # 両方ある
                # leftを更新、値を更新
                next_left = 0
                for j in range(s, t):
                    d = (a_list_s[j] >> i) & 1
                    if d == 1 and next_left == 0:
                        next_left = j
                    if d == 1:
                        left[j] = next_left
                    max_v[j] = max_v[j] | (1 << i)
            else:
                # 片方しかない
                # leftを更新不要
                # 値は小さくする
                if r == 2:
                    for j in range(s, t):
                        max_v[j] ^= (1 << i)
            s = t
        # print(max_v)
    return min(max_v)


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [12, 18, 11]) == 16
    assert solve(10, [0] * 10) == 0
    assert solve(5, [324097321, 555675086, 304655177, 991244276, 9980291]) == 805306368


if __name__ == "__main__":
    test()
    main()
