from copy import deepcopy
from collections import deque

dx, dy = [1,-1,0,0],[0,0,-1,1]
def findEnterance(Map, keys, H, W):
    start = []
    for x in range(W):
        if Map[0][x] != '*':
            if Map[0][x] == '.' or (97 <= ord(Map[0][x]) and ord(Map[0][x]) <= 123) or Map[0][x] == '$': # 대문자이면
                start.append((0, x))
            elif 65 <= ord(Map[0][x]) and ord(Map[0][x]) <= 91: # 대문자이면
                if Map[0][x] in keys:
                    start.append((0, x))
    
    for x in range(W):
        if Map[H-1][x] != '*':
            if Map[H-1][x] == '.' or (97 <= ord(Map[H-1][x]) and ord(Map[H-1][x]) <= 123) or Map[H-1][x] == '$': # 대문자이면
                start.append((H-1, x))
            elif 65 <= ord(Map[H-1][x]) and ord(Map[H-1][x]) <= 91: # 대문자이면
                if Map[H-1][x] in keys:
                    start.append((H-1, x))
                    
    for y in range(H):
        if Map[y][0] != '*':
            if Map[y][0] == '.' or (97 <= ord(Map[y][0]) and ord(Map[y][0]) <= 123) or Map[y][0] == '$': # 대문자이면
                start.append((y, 0))
            elif 65 <= ord(Map[y][0]) and ord(Map[y][0]) <= 91: # 대문자이면
                if Map[y][0] in keys:
                    start.append((y, 0))
        
        if Map[y][W-1] != '*':
            if Map[y][W-1] == '.' or (97 <= ord(Map[y][W-1]) and ord(Map[y][W-1]) <= 123) or Map[y][W-1] == '$': # 대문자이면
                start.append((y, W-1))
            elif 65 <= ord(Map[y][W-1]) and ord(Map[y][W-1]) <= 91: # 대문자이면
                if Map[y][W-1] in keys:
                    start.append((y, W-1))
        
    
    
    return start
            
def bfs(y,x,_keys,Map,visited,H,W):
    answer = 0
    q = deque((y, x, _keys))
    visited[y][x]=True
    
    while q:
        _y , _x, keys = q.popleft()
        if Map[_y][_x] == '$':
            answer += 1
        else:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny == 0 or nx == 0 or ny == H or nx == W or visited[ny][nx]:
                    continue
                if 65 <= ord(Map[ny][nx]) and ord(Map[ny][nx]) <= 91:
                
    

if __name__ == "__main__":
    for _ in range(int(input())):
        H, W = map(int,input().split())
        visited = [[False for _ in range(W)] for _ in range(H)]
        Map = []
        answer = 0
        for _ in range(H):
            Map.append(input())
        keys = input()
        
        for y, x in findEnterance(Map, keys, H, W):
            answer = max(bfs(y, x, keys,Map,visited,H,W), answer)
        
        
        print(answer)
        
            