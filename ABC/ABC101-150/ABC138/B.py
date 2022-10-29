N = int(input())
A_list = list(map(int, input().split()))

print(1 / sum([1 / a for a in A_list]))
