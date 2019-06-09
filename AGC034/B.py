s = list(input())

# count BC from left
bc_cnt = 0
res = 0
for i in range(len(s)-2, -1, -1):
    if s[i] == "B":
        if s[i+1] == "C":
            bc_cnt += 1
        else:
            bc_cnt = 0
    elif s[i] == "A":
        if s[i+1] == "C":
            bc_cnt = 0
    else:
        if s[i+1] == "C":
            bc_cnt = 0
    if s[i] == 'A':
        res += bc_cnt
print(res)
