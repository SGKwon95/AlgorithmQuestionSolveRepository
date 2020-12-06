# 미친 로봇
P = [0, 0, 0, 0]
N, P[0], P[1], P[2], P[3] = map(int,input().split())
dx, dy = [1,-1,0,0], [0,0,-1,1]

for i in range(4):
    P[i] /= 100

Map = [[False for _ in range(2*N+1)] for _ in range(2*N+1)]

answer = 0

def dfs(y, x, result, cnt):
    global answer
    if cnt == N:
        answer += result
        return
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not Map[ny][nx]:
            Map[ny][nx]=True
            dfs(ny,nx,result * P[i], cnt+1)
            Map[ny][nx]=False
            
Map[N][N]=True
dfs(N,N,1,0)
print(answer)