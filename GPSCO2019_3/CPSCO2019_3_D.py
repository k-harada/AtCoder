N = int(input())
S = list(input())



res = "Yes"

# first must be red
if S[0] != "R":
    res = "No"

# next color rule
# R -> R or G
# G -> R or B
# B -> any
for i in range(N - 1):
    check = S[i] + S[i + 1]
    if check == "RB" or check == "GG":
        res = "No"

# last must be blue
if S[-1] != "B":
    res = "No"

print(res)