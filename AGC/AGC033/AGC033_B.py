H, W, N = map(int, input().split())
sr, sc = map(int, input().split())
S = list(input())
T = list(input())

border_U = 0
border_D = H + 1
border_L = 0
border_R = W + 1

res = "YES"

for i in range(N-1):

    # Takahashi's turn
    if S[N - 1 - i] == "U":
        border_U += 1
    elif S[N - 1 - i] == "D":
        border_D -= 1
    elif S[N - 1 - i] == "L":
        border_L += 1
    elif S[N - 1 - i] == "R":
        border_R -= 1

    # mate in the middle
    if border_U >= border_D - 1 or border_L >= border_R - 1:
        res = "NO"

    # Aoki's turn
    if T[N - 2 - i] == "U":
        border_D += 1
    elif T[N - 2 - i] == "D":
        border_U -= 1
    elif T[N - 2 - i] == "L":
        border_R += 1
    elif T[N - 2 - i] == "R":
        border_L -= 1

    # sanitize
    border_U = max(border_U, 0)
    border_D = min(border_D, H + 1)
    border_L = max(border_L, 0)
    border_R = min(border_R, W + 1)
    # print(border_U, border_D, border_L, border_R)

# Takahashi's final turn
if S[0] == "U":
    border_U += 1
elif S[0] == "D":
    border_D -= 1
elif S[0] == "L":
    border_L += 1
elif S[0] == "R":
    border_R -= 1

if sr <= border_U:
    res = "NO"
elif sr >= border_D:
    res = "NO"
elif sc <= border_L:
    res = "NO"
elif sc >= border_R:
    res = "NO"

# print(border_U, border_D, border_L, border_R)
print(res)