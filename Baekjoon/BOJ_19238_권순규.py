#스타트 택시
comment = '''
시간 많이 걸리긴 했는데 한번에 통과 성공
문제 예제를 그대로 구현하였다
먼저 예제 입력을 받은 다음에
어떤 승객을 태울지를 nextGuest()를 통하여 정한다.
이 때 반드시 태운 승객은 리스트에서 삭제해야 한다.

그 다음에 bfs()에서 시작 위치를 반환한 리스트로 정하고
그 위치에서 bfs()를 돌린다
이걸 M만큼 반복하면 된다.
중간에 실패하면 바로 종료시키면 된다.
'''


from collections import deque
from copy import deepcopy
N,M,fuel = 0,0,0 #M은 승객 수
Map = []
_visited = []
destination = []
guest = []
startTaxi = [0,0]
dx, dy = [1,-1,0,0],[0,0,-1,1]

def nextGuest(): # 다음 승객의 좌표 반환
    global startTaxi, guest, _visited
    
    visited = deepcopy(_visited)
    
    flag = False # 운행 가능한지 여부, 즉 벽에 막혀서 못가면 False가 된다.
    for i in guest: # 처음에 택시와 승객들간의 거리를 -1로 초기화
        i[2] = -1
    
    q = deque([[startTaxi[0], startTaxi[1], 0]]) # 마지막 원소는 이동 거리
    visited[startTaxi[0]][startTaxi[1]] = True
    
    while q:
        y, x, d = q.popleft()
        
        for g in guest:
            if y == g[0] and x == g[1]:
                g[2] = d
                flag = True
                break
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny == N or nx == N:
                continue
            if not visited[ny][nx] and Map[ny][nx] == 0:
                visited[ny][nx] = True
                q.append([ny,nx,d+1])
    
    if not flag:
        return [-1, -1, -1, -1]
    else:
        guest.sort(key=lambda x:(-x[2],-x[0],-x[1])) #거리, 행, 열순으로 내림차순 정렬
        return guest.pop() # 태운 승객은 반드시 pop하여 삭제해야 한다.
        
def bfs():
    global _visited, fuel,startTaxi, destination
    ng = nextGuest()
    if ng == [-1,-1,-1, -1]:
        return False
    flag=False
    visited = deepcopy(_visited)
    
    q = deque([[ng[0],ng[1],fuel-ng[2], 0]]) # 마지막 원소는 이동 거리
    
    visited[ng[0]][ng[1]] = True
    # print('desination=',destination[ng[3]][0],',',destination[ng[3]][1])
    # print('fuel=',fuel)
    while q:
        y, x, f, d = q.popleft()
        
        if [y,x] == destination[ng[3]] and f >= 0:
            f += 2*d
            fuel = f
            flag = True
            break        
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny == N or nx == N:
                continue
            if not visited[ny][nx] and Map[ny][nx] == 0:
                visited[ny][nx] = True
                q.append([ny,nx,f-1,d+1])
    
    if flag:
        startTaxi = destination[ng[3]]
        # print('startTaxi=',startTaxi)
        return True
    else: return False
    
    

if __name__ == "__main__":
    N, M, fuel = map(int,input().split())
    for _ in range(N):
        Map.append(list(map(int,input().split())))
    
    _visited = [[False for _ in range(N)] for _ in range(N)]
    
    startTaxi = list(map(int,input().split()))
    startTaxi[0] -= 1
    startTaxi[1] -= 1
    for i in range(M):
        tmp = list(map(int,input().split()))
        guest.append([tmp[0]-1,tmp[1]-1, -1, i]) # 마지막에 i를 삽입한 이유는 destination 인덱스와 매칭하기 위함
        destination.append([tmp[2]-1,tmp[3]-1])
        
    for _ in range(M):
        if not bfs():
            fuel = -1
            break
        
    print(fuel)
        
        