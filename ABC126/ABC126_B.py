S = list(input())

A = int(S[0]) * 10 + int(S[1])
B = int(S[2]) * 10 + int(S[3])

if A > 0 and A <= 12:
    res_A = True
else:
    res_A = False

if B > 0 and B <= 12:
    res_B = True
else:
    res_B = False

if res_A and res_B:
    print("AMBIGUOUS")
elif res_A:
    print("MMYY")
elif res_B:
    print("YYMM")
else:
    print("NA")
