# A
L, X = map(int, input().split())

# 2L -> 0
X = X % (2 * L)
if X <= L:
    print(X)
else:
    print(2 * L - X)