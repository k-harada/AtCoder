N = int(input())
H_list = list(map(int, input().split()))

r = 0
res = 0
for i in range(N - 1):
    if H_list[i] >= H_list[i + 1]:
        r += 1
        if r > res:
            res = r
    else:
        r = 0

if __name__ == "__main__":
    print(res)
