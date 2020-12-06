import sys
M, N = 0,0
Map = []
dp = []
dx, dy = [1,-1,0,0],[0,0,-1,1]

def dfs(y,x):
    dp[y][x] += 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if Map[ny][nx] and Map[ny][nx] < Map[y][x]:
            dfs(ny,nx)

if __name__ == "__main__":
    M, N = map(int,input().split())
    Map = []
    dp = [[0 for _ in range(N+2)] for _ in range(M+2)]
    Map.append([0 for _ in range(N+2)])
    for _ in range(M):
        Map.append([0] + list(map(int,sys.stdin.readline().split())) + [0])
    Map.append([0 for _ in range(N+2)])

    dfs(1,1)
    
    print(dp[M][N])
    
                

