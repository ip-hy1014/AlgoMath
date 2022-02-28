from collections import Counter
n = int(input())
a = list(map(int,input().split()))
c = Counter(a)
ans = 0
for i in c:
  if i == 50000:
    ans += c[i] * (c[i]-1)
  else:
    ans += c[i] * c[100000-i]
print(ans//2)