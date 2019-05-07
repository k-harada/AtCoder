N = int(input())
S = list(input())
A, B, C, D = map(int, input().split())

# A : ox
# B : xo
# C : o
# D : x

# split into sequences
# oxoxo ... oxo -> o + any
# xoxox ... xox -> x + any
# oxoxo ... xox -> o + x + any or all ox
# xoxox ... oxo -> o + x + any or all xo

cnt_x = 0
cnt_o = 0
cnt_any = 0
cnt_xo_list = []
cnt_ox_list = []

st = 0
for i in range(1, N):
    # split
    if S[i] == S[i - 1]:
        if st == i - 1:
            if S[st] == "o":
                cnt_o += 1
            else:
                cnt_x += 1
        elif S[i] != S[st]:
            if S[st] == "o":
                cnt_ox_list.append((i - st) // 2)
            else:
                cnt_xo_list.append((i - st) // 2)
        else:
            if S[st] == "o":
                cnt_o += 1
                cnt_any += (i - st) // 2
            else:
                cnt_x += 1
                cnt_any += (i - st) // 2
        st = i

# last
if st == N - 1:
    if S[st] == "o":
        cnt_o += 1
    else:
        cnt_x += 1
elif S[-1] != S[st]:
    if S[st] == "o":
        cnt_ox_list.append((N - st) // 2)
    else:
        cnt_xo_list.append((N - st) // 2)
else:
    if S[st] == "o":
        cnt_o += 1
        cnt_any += (N - st) // 2
    else:
        cnt_x += 1
        cnt_any += (N - st) // 2

# print(cnt_x, cnt_o, cnt_any, cnt_xo_list, cnt_ox_list)

# check
res = "Yes"

# use xo for xo_list from smaller
cnt_xo_list_s = list(reversed(sorted(cnt_xo_list)))
while len(cnt_xo_list_s) > 0:
    cnt = cnt_xo_list_s.pop()
    if B >= cnt:
        # use xo
        B -= cnt
    else:
        # break xo_list
        total = sum(cnt_xo_list_s) + cnt
        cnt_ = len(cnt_xo_list_s) + 1
        C -= cnt_
        D -= cnt_
        cnt_any += total - cnt_
        break

cnt_ox_list_s = list(reversed(sorted(cnt_ox_list)))
while len(cnt_ox_list_s) > 0:
    cnt = cnt_ox_list_s.pop()
    if A >= cnt:
        # use xo
        A -= cnt
    else:
        # break xo_list
        total = sum(cnt_ox_list_s) + cnt
        cnt_ = len(cnt_ox_list_s) + 1
        C -= cnt_
        D -= cnt_
        cnt_any += total - cnt_
        break

if cnt_any < A + B:
    res = "No"
else:
    cnt_any -= (A + B)
    A = 0
    B = 0
    C -= cnt_any
    D -= cnt_any
if C != cnt_o:
    res = "No"
if D != cnt_x:
    res = "No"

print(res)
