n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      for l in range(k+1,n):
        for m in range(l+1,n):
          if a[i]+a[j]+a[k]+a[l]+a[m]==1000:
            ans+=1
print(ans)

#別解
n = int(input())
a = list(map(int,input().split()))
from itertools import combinations
ans = 0
for a,b,c,d,e in combinations(a,5):
  if a+b+c+d+e==1000:
    ans+=1
print(ans)