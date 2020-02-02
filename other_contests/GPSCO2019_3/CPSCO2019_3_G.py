# 解説みた
# これはTLE

from heapq import heappop, heappush
from fractions import Fraction

N, X = map(int, input().split())
a_list = list(map(int, input().split()))
A = sum(a_list)

h = []

# heappush
for i in range(N):
    a = a_list[i]

    # lower
    s = a * X // A
    heappush(h, (Fraction(-1, a), -i, s))

    # middle
    if a * X % A != 0:
        t = s + 1
        dif = abs(Fraction(t, a) - Fraction(X, A)) - abs(Fraction(s, a) - Fraction(X, A))
        heappush(h, (dif, -i, 1))

    # rest
    heappush(h, (Fraction(1, a), -i, X))

# heappop
x_list = [0] * N
total = 0

while True:
    v, i, c = heappop(h)
    if total + c > X:
        c = X - total
    x_list[-i] += c
    total += c
    if total == X:
        break

for x in x_list:
    print(x)
