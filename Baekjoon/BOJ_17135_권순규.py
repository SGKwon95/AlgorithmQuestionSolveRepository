from collections import deque
from copy import deepcopy
Map = []
_Map = []
N,M,D = 0,0,0
answer = 0
dx,dy = [1,-1,0,0],[0,0,-1,1]   

def cal(position):
    global Map
    enemy = []
    numofEnemy = 0
    for i in position:
        tmp = bfs(i)
        if tmp != -1:
            enemy.append(tmp)
    
    for i in enemy:
        if Map[i[0]][i[1]] == 1:
            Map[i[0]][i[1]] = 0
            numofEnemy += 1
        
    return numofEnemy

def bfs(i):
    global Map
    enemy = []
    visited = [[False for _ in range(M)] for _ in range(N)]
    q = deque([[N-1,i,1]])
    visited[N-1][i] = True
    while q:
        y,x,d = q.popleft()
        
        if Map[y][x] == 1:
            enemy.append((y,x,d))
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny == N or nx == M:
                continue
            
            if not visited[ny][nx] and d < D:
                visited[ny][nx] = True
                q.append([ny,nx,d+1])
                
    enemy.sort(key=lambda x:(-x[2],-x[1]))
    #print('target=',enemy)
    if enemy:
        return enemy.pop()
    else:
        return -1
        
        
            
def EnemyDown():
    for i in range(N-1,0,-1):
        Map[i] = Map[i-1]
    Map[0] = [0] * M
    

if __name__== "__main__":
    N, M, D = map(int,input().split())
    
    for _ in range(N):
        _Map.append(list(map(int,input().split())))
        
    for i in range(M):
        for j in range(i+1,M):
            for k in range(j+1,M):
                position = [i,j,k]
                tmp = 0
                Map = deepcopy(_Map)
                for l in range(N):
                    tmp += cal(position)
                    if l < N-1:
                        EnemyDown()
                    
                answer = max(answer,tmp)

    print(answer)
