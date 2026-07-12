def solve(n, k):
    if 2 ** n < k:
      return -1
    count = [0]
    for i in range(1, 8):
        if k > (10 ** i) - 1:
            count.append(9 * (10 ** (i - 1)))
        elif 10 ** (i - 1) < k:
            count.append(k - (10 ** (i - 1)))
        else:
            count.append(0)
    # print(count)
    res = 0
    ncr = 1
    for i in range(1, n + 1):
        ncr *= (n - i + 1)
        ncr //= i
        xxx = ncr
        # print("ncr", ncr)
        for j in range(7, -1, -1):
            if count[j] <= xxx:
                res += i * j * count[j]
                xxx -= count[j]
                count[j] = 0
            else:
                res += i * j * xxx
                count[j] -= xxx
                xxx = 0
        # print(count)
        # print(res)
        if count[1] == 0:
          break
    # print(res)
    return res


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        res = solve(n, k)
        print(res)
    

def test():
    assert solve(3, 5) == 5
    assert solve(100, 25) == 39
    assert solve(5, 1225) == -1
    assert solve(100, 101) == 192
    assert solve(5, 32) == 126
    assert solve(180, 998244) == 17655598
    


if __name__ == "__main__":
    test()
    main()
