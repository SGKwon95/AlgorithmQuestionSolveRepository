import sys
N = int(input())
T,P = [],[]
dp = [0]*(1500051)
for _ in range(N):
    t,p = map(int,sys.stdin.readline().split())
    T.append(t)
    P.append(p)

for i in range(N):
    # i일에 상담하면 그 다음 상담은 i+T[i] 일에 할 수 있다.
    dp[i+T[i]] = max(dp[i+T[i]],dp[i]+P[i])
    # 상담하지 않았을 경우
    dp[i+1] = max(dp[i+1],dp[i])

print(dp[N])