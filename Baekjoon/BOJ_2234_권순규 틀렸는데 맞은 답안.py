#성곽
from collections import deque
N, M = 0,0
Map = []
visited = []
numofRoom = 0
maxRoomArea = 0
maxRoomArea2 = 0

# 남동북서
dx, dy = [0,1,0,-1],[1,0,-1,0]

def isWall(n):
    # 남동북서
    lst = [False, False, False, False]
    num = [8,4,2,1]
    for i in range(4):
        if n & num[i]:
            lst[i] = True
    
    return lst

def bfs2(_y, _x):
    global N, M, visited, Map
    
    roomArea = 0
    
    q = deque([[_y, _x]])
    visited[_y][_x][1] = True
    
    while q:
        y, x = q.popleft()
        wall = isWall(Map[y][x])
        roomArea += 1
        
        if visited[y][x][0]:
            return 0
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny == M or nx == N:
                continue
            if not visited[ny][nx][1] and not wall[i]:
                visited[ny][nx][1] = True
                q.append([ny, nx])
    
    #print('-',roomArea)                
    return roomArea
    
    
def bfs(_y, _x):
    global N, M, visited, Map
    
    roomArea = 0
    roomArea2 = 0
    
    q = deque([[_y, _x]])
    visited[_y][_x][0] = True
    
    while q:
        y, x = q.popleft()
        wall = isWall(Map[y][x])
        roomArea += 1
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny == M or nx == N:
                continue
            if wall[i]:
                if not visited[ny][nx][1]:
                    roomArea2 = max(bfs2(ny,nx),roomArea2)
            else:
                if not visited[ny][nx][0]:
                    visited[ny][nx][0] = True
                    q.append([ny,nx])
    #print('roomArea=',roomArea)                
    #print('roomArea2=',roomArea2)
    return roomArea, roomArea2            

if __name__ == "__main__":
    N, M = map(int,input().split())
    for _ in range(M):
        Map.append(list(map(int,input().split())))
    visited = [[[False, False] for _ in range(N)] for _ in range(M)]
    
    for y in range(M):
        for x in range(N):
            if not visited[y][x][0]:
                roomArea, roomArea2 = bfs(y,x)
                maxRoomArea = max(maxRoomArea, roomArea)
                maxRoomArea2 = max(maxRoomArea2, roomArea + roomArea2)
                numofRoom += 1
    
    print(numofRoom)
    print(maxRoomArea)
    print(maxRoomArea2)
                
    
    