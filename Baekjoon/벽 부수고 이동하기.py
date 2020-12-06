# 2206
from collections import deque
N, M = 0, 0
Map = []
visited = []
dx, dy = [1,-1,0,0],[0,0,-1,1]

def bfs():
    global visited
    answer = -1
    q = deque([[0,0,1,False]])
    visited[0][0][0] = True
    
    while q:
        y, x, d, c = q.popleft()
        
        if (y,x) == (N-1,M-1):
            answer = d
            break
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny == N or nx == M:
                continue
            if c:
                if not visited[ny][nx][1] and Map[ny][nx] == '0':
                    visited[ny][nx][1] = True
                    q.append([ny,nx,d+1,c])
            else:
                if Map[ny][nx] == '0' and not visited[ny][nx][0]:
                    visited[ny][nx][0] = True
                    q.append([ny,nx,d+1,c])
                elif Map[ny][nx] == '1' and not visited[ny][nx][1]:
                    visited[ny][nx][1] = True
                    q.append([ny,nx,d+1,True])
                    
    return answer   

if __name__ == '__main__':
    N, M = map(int,input().split())
    for _ in range(N):
        Map.append(input())
    visited = [[[False, False] for _ in range(M)] for _ in range(N)]
    print(bfs())