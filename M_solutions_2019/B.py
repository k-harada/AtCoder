S = list(input())

count_x = 0
for s in S:
    if s == 'x':
        count_x += 1

if count_x >= 8:
    print("NO")
else:
    print("YES")
