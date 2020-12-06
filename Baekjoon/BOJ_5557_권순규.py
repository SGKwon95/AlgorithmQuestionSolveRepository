#1학년
#dp[i][j] = i번째 등식에서 j을 계산할때 결과가 0이상 20이하인지여부의 개수

N = int(input())
arr = list(map(int,input().split()))
dp = [[0 for _ in range(21)] for _ in range(N-1)]
dp[0][arr[0]] = 1
for y in range(N-2):
    for x in range(21):
        if dp[y][x]: #0이 아니면
            if 0 <= (x + arr[y+1]) <= 20: #원래는 연속 부등호는 0<a and a<b 이렇게 써야하지만 python은 그냥 써도 된다.
                dp[y+1][x+arr[y+1]] += dp[y][x]
            if 0 <= (x - arr[y+1]) <= 20:
                dp[y+1][x-arr[y+1]] += dp[y][x]

print(dp[N-2][arr[N-1]])
