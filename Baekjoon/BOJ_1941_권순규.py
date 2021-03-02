'''
소문난 칠공주 1941
문제 유형 : bfs,dfs,백트래킹, 브루트포스
로직 :
1. 25명의 사람중 7명을 뽑는다
2. 이 7명의 사람이 모두 상하좌우로 붙어있는지, 붙어있으면 S가 4이상인지 검사한다.
3. 2의 조건을 만족시킨 경우의 수를 카운트하여 합산한다
'''

def bfs(comb):
    linked = [[False] * 5 for _ in range(5)]
    visited = [[False] * 5 for _ in range(5)]
    start = comb[0]
    for c in comb:
        linked[c[0]][c[1]] = True
    visited[start[0]][start[1]] = True
    q = deque([start])
    S = 0
    Y = 0
    
    while q:
        (y,x) = q.popleft()
        
        if people[y][x] == 'S':
            S += 1
        else:
            Y += 1
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or nx < 0 or ny == 5 or nx == 5:
                continue
            
            if linked[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny,nx))
 
    return True if S+Y == 7 and Y < 4 else False
    

dx,dy = (1,-1,0,0),(0,0,-1,1)
from itertools import combinations
from collections import deque
people = []
for _ in range(5):
    people.append(input())

answer = 0
comb = []                    
for y in range(5):
    for x in range(5):
        comb.append((y,x))


for c in combinations(comb,7):
    if bfs(c):
        answer += 1

print(answer)
