S = list(input())

res = 'Good'

for i in range(3):
    if S[i] == S[i+1]:
        res = 'Bad'

print(res)
