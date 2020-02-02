S = list(input())
T = []
for s in S:
    if s == "O":
        T.append("A")
    elif s == "A":
        T.append("O")
    else:
        T.append(s)
print("".join(T))