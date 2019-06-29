S = list(input())
S_cnt = dict()

for s in S:
    if s in S_cnt.keys():
        S_cnt[s] += 1
    else:
        S_cnt[s] = 1

res = 'Yes'
for s in S_cnt.keys():
    if S_cnt[s] != 2:
        res = 'No'
print(res)