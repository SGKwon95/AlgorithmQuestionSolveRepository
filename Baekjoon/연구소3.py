dx, dy = [1,-1,0,0],[0,0,-1,1]

def bfs(start):
    n = len(start)
    
    for i in start:
        timeMap[i[0]][i[1]] = 0
        
    q = deque([])
    
    for i in start:
        q.append([i,0])
    
    answer = -1
    
    while q:
        for _ in range(n):
            if not q:
                return answer
            (y,x),t = q.popleft()
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny == N or nx < 0 or nx == N:
                    continue
                if timeMap[ny][nx] == -1:
                    if Map[ny][nx] == 0:
                        q.append([(ny,nx),t+1])
                        timeMap[ny][nx] = t+1
                        answer = t+1
                    elif Map[ny][nx] == 2:
                        meetVirus(ny,nx,t,q)
                        
    return answer

def meetVirus(y,x,t,q):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny == N or nx < 0 or nx == N:
            continue
        if timeMap[ny][nx] == -1:
            if Map[ny][nx] == 0:
                q.append([(ny,nx),t+1])
                timeMap[ny][nx] = t+1
                answer = t+1
            elif Map[ny][nx] == 2:
                meetVirus(ny,nx,t)
                

from itertools import combinations
from collections import deque
if __name__ == "__main__":
    N, M = map(int,input().split())
    Map = [[] for _ in range(N)]
    timeMap = [[-1 for _ in range(N)] for _ in range(N)]
    canLocateVirus = []
    answer = int(1e9)
    for y in range(N):
        for x, i in enumerate(list(map(int,input().split()))):
            if i == 2:
                canLocateVirus.append((y,x))
            Map[y].append(i)
    
    for comb in combinations(canLocateVirus,M):
        tmp = bfs(comb)
        if tmp != -1:
            answer = min(answer,tmp)
        timeMap = [[-1 for _ in range(N)] for _ in range(N)]
    
    if answer == int(1e9):
        print(-1)
    else:
        print(answer)
        