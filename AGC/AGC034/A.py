N, A, B, C, D = map(int, input().split())
S = list(input())

res = 'Yes'
# case 1
if C < D:
    for i in range(A-1, C-1):
        if S[i] == '#' and S[i+1] == '#':
            res = 'No'
    for i in range(B-1, D-1):
        if S[i] == '#' and S[i+1] == '#':
            res = 'No'
else:
    cnt = 0
    for i in range(B-2, D-1):
        if S[i] == '.' and S[i+1] == '.' and S[i+2] == '.':
            cnt += 1
    if cnt == 0:
        res = 'No'
    for i in range(A-1, C-1):
        if S[i] == '#' and S[i+1] == '#':
            res = 'No'

print(res)
