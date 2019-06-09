L = list(input())
LARGE = 10**9 + 7

res = 0
cum_one = 0
for i in range(len(L)):
    if L[i] == '1':
        res += pow(2, cum_one, LARGE) * pow(3, len(L) - i - 1, LARGE)
        res = res % LARGE
        cum_one += 1
# last
res += pow(2, cum_one, LARGE)
res = res % LARGE
print(res)
