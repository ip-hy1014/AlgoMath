n,s = map(int,input().split())
a = list(map(int,input().split()))
dp = [False]*(s+1)
dp[0] = True
for i in a:
  for j in range(s,-1,-1):
    if dp[j] and i+j<=s:
      dp[i+j] = True
print("Yes" if dp[s] else "No")