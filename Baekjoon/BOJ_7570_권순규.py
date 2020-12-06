#줄 세우기
#LIS 문제
#가장 긴 증가수열을 찾되 연속(1,2,3,4...)이어야 함
N = int(input())
children = list(map(int,input().split()))
dp = [0] * (N+1)
for i in range(N):
    dp[children[i]] = dp[children[i]-1] + 1
    
print(N-max(dp))