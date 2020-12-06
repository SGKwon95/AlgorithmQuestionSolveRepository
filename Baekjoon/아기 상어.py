from collections import deque
from copy import deepcopy
N = 0
Map = []
fish = []
_visited = []
startLoc = [-1,-1]
sharkSize = 2
eat = 0
dx, dy = [1,-1,0,0],[0,0,-1,1]
answer = 0
errorCode = [-1,-1,-1,-1]
def nextTarget(sl): #먹을 수 있는지는 고려하지 않고 우선 단순하게 거리만 계산하기
    global fish
    visited = deepcopy(_visited)
    
    flag = False
    for i in fish:
        i[3] = 777
    
    q = deque([[sl[0],sl[1],0]])
    visited[sl[0]][sl[1]] = True
    
    while q:
        y,x,d = q.popleft()
        
        for f in fish:
            if [y,x] == [f[0],f[1]]:
               f[3] = d
               flag = True
               break
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny == N or nx == N:
                continue
            if not visited[ny][nx] and Map[ny][nx] <= sharkSize:
                visited[ny][nx] = True
                q.append([ny,nx,d+1])
                        
    if flag: 
        fish.sort(key=lambda x:(x[3],x[0],x[1]))
        #print(fish)
        for i in range(len(fish)):
            if fish[i][2] < sharkSize and fish[i][3] != 777: #거리가 설정되지 않았던 경우를 고려하지 않아서 틀렸음
                tmp = fish[i]
                del fish[i]
                return tmp
    return errorCode
    
    

def bfs():
    global startLoc, eat, sharkSize, Map
    target = nextTarget(startLoc)
    #print(target)
    if target == errorCode:
        return -1
    eat += 1
    if eat == sharkSize:
        eat = 0
        sharkSize += 1
    startLoc = [target[0],target[1]]
    Map[target[0]][target[1]] = 0
    
    return target[3]


if __name__ == "__main__":
    N = int(input())
    _visited = [[False for _ in range(N)] for _ in range(N)]
    for y in range(N):
        tmp = list(map(int,input().split()))
        Map.append(tmp)
        for x in range(N):
            if 1 <= tmp[x] and tmp[x] <=6:
                fish.append([y,x,tmp[x],-1])
            elif tmp[x] == 9:
                startLoc = [y,x]
                Map[y][x] = 0 #9의 좌표를 저장했으므로 없애준다.
                
    for _ in range(len(fish)):
        tmp = bfs()
        if tmp == -1:
            break
        else:
            answer += tmp
        
    print(answer)
        