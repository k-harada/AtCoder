from operator import itemgetter


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
XY.sort(key=itemgetter(1))
for i in range(N):
    XY[i][1] = i
XY.sort(key=itemgetter(0))

y_nor_list = [xy[1] for xy in XY]

sg_left = Bit(N)
sg_right = Bit(N)

left_lower = [0] * N
left_upper = [0] * N
right_lower = [0] * N
right_upper = [0] * N

for i in range(N):
    c = y_nor_list[i] + 1
    left_lower[i] = sg_left.sum(c)
    left_upper[i] = i - left_lower[i]
    sg_left.add(c, 1)

for i in range(N-1, -1, -1):
    c = y_nor_list[i] + 1
    right_lower[i] = sg_right.sum(c)
    right_upper[i] = N - 1 - i - right_lower[i]
    sg_right.add(c, 1)

# print(left_lower)
# print(left_upper)
# print(right_lower)
# print(right_upper)

LARGE = 998244353

pow2m1 = [0] * (N + 1)
for i in range(1, N + 1):
    pow2m1[i] = (2 * pow2m1[i - 1] + 1) % LARGE

res = 0
for i in range(N):
    r = pow2m1[N]
    r -= pow2m1[left_lower[i] + left_upper[i]]
    r -= pow2m1[right_lower[i] + right_upper[i]]
    r -= pow2m1[left_lower[i] + right_lower[i]]
    r -= pow2m1[left_upper[i] + right_upper[i]]
    r += pow2m1[left_lower[i]]
    r += pow2m1[left_upper[i]]
    r += pow2m1[right_lower[i]]
    r += pow2m1[right_upper[i]]
    res += r

print(res % LARGE)
