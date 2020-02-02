N = int(input())
S = list(input())

LARGE = 10 ** 9 + 7

res = 1
arrows = 0

for i in range(2 * N):
    if arrows == 0 and S[i] == "W":
        res = 0
        break
    if S[i] == "B" and arrows % 2 == 0:
        arrows += 1
    elif S[i] == "W" and arrows % 2 == 1:
        arrows += 1
    else:
        res *= arrows
        res %= LARGE
        arrows -= 1

if arrows > 0:
    res = 0


for i in range(1, N + 1):
    res *= i
    res %= LARGE

if __name__ == "__main__":
    print(res)
