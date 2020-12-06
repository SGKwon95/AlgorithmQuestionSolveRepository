N, K = map(int,input().split())

d=[[0 for _ in range(K+1)] for _ in range(N+1)]
w,v = [0],[0]

for _ in range(N):
    _w, _v = list(map(int,input().split()))
    w.append(_w)
    v.append(_v)

def printDP(i,j):
    for k in d:
        print(k)
    print('i={}, j={}, 남은 무게={}, {}번째 물건의 무게={}, 가치={}'.format(i,j,j-w[i],i,w[i],v[i]))
    print()
	
for i in range(1,N+1):
    for j in range(1,K+1):
        d[i][j] = d[i-1][j]
        if j-w[i] >= 0:
            d[i][j] = max(d[i][j],d[i-1][j-w[i]]+v[i])
        printDP(i,j)
          
currentWorth = d[N][K]
answer = []
i = N
while i:
    for j in range(1,K+1):
        if currentWorth-v[i] == d[i-1][j]:
            answer.append(i)
            currentWorth = d[i-1][j]
            break
    i -= 1

print(d[N][K])
print(answer)



'''
D[i][j] : i번째 물건까지 고려했고, 배낭에 넣은 물건의 무게 합이 j일때 가치의 최대값
그러면 i번째 물건을 가방에 넣지 않으면 그 때의 무게는 D[i-1][j]
i번째 물건을 가방에 넣었으면 D[i-1][j-w[i]] + v[i]


for i in range(1,N+1):
    for j in range(1,K+1):
        d[i][j] = d[i-1][j]
        if j-w[i] >= 0:
            d[i][j] = max(d[i][j],d[i-1][j-w[i]]+v[i])
'''

'''
N, K = map(int,input().split())

dp=[0] * (K+1)
weight,worth = [0],[0]

for _ in range(N):
    w, t = list(map(int,input().split()))
    weight.append(w)
    worth.append(t)
	
for i in range(1,N+1):
    for j in range(K,0,-1):
        if j-weight[i]>=0:
            dp[j] = max(dp[j],dp[j-weight[i]]+worth[i])
          

print(dp[K])
'''
'''

'''