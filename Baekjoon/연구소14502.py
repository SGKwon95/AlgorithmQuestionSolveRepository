'''
https://www.acmicpc.net/problem/14502
'''
def bfs(loc):
    deleted = 0
    visited[loc[0]][loc[1]] = True
    queue = deque([loc])
    
    while queue:
        (y,x) = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or nx < 0 or ny == N or nx == M:
                continue
            
            if not visited[ny][nx] and copied_map[ny][nx] == 0:
                visited[ny][nx] = True
                deleted += 1
                queue.append((ny,nx))
    
    return deleted

from itertools import combinations
from copy import deepcopy
from collections import deque
if __name__ == "__main__":
    dx, dy = (1,-1,0,0),(0,0,-1,1)
    N, M = map(int,input().split())
    Map = []
    virus = []
    canLocateWalls = []
    for y in range(N):
        tmp = list(map(int,input().split()))
        for x, i in enumerate(tmp):
            if i == 2:
                virus.append((y,x))
            elif i == 0:
                canLocateWalls.append((y,x))
                
        Map.append(tmp)
    initAreaSize = len(canLocateWalls)-3
    answer = 0
    
    for comb in combinations(canLocateWalls,3):
        tmp = 0
        visited = [[False for _ in range(M)] for _ in range(N)]
        copied_map = deepcopy(Map)
        for w in comb:
            copied_map[w[0]][w[1]] = 1
        for vir in virus:
            tmp += bfs(vir)
        
        answer = max(answer,initAreaSize-tmp)
    
    print(answer)
        
        
    
    
    
    
    
        