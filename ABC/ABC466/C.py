n = int(input())

res = 0
i = 1
j = 2
while j <= n:
  print(f"? {i} {j}")
  r = input()
  if r == "Yes":
    res += j - i
    j += 1
  else:
    i += 1
  if i == j:
    j += 1

print(f"! {res}")
