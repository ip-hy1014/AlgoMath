from collections import Counter
n = int(input())
a = list(map(int,input().split()))
c = Counter(a)
ans = 0
for i in c.values():
  ans += i*(i-1)//2
print(ans)