#성곽
comment = '''
풀이과정:
처음에는 1번, 2번 문제를 dfs로 접근 하였음. 방향벡터를 잘못 적어서 디버깅하느라 애썼다.
남쪽으로 가는거를 수학에서의 좌표평면을 생각해버려서 (x,y) = (0,1)이 아닌 (0,-1)로 생각하느라 시간 버림 ㅎ
이후 여차저차 디버깅하였으나 3번문제에서 dfs로 풀 수 없음을 깨달음
저번에 풀었던 벽뚫기 문제는 반드시 bfs로만 풀 수 있었기 때문
그래서 bfs로 바꾸었고 벽을 만났으면 dfs로 새로운 탐색을 하려고 했으나
dfs는 특성상 리턴값을 반환하기 힘들어서 그 공간에 다시 bfs를 돌리는 것으로 해결함
근데 생각해보니 처음에 dfs돌리고 벽 뚫었을때 bfs돌리면 됐었네? ㅎㅎ 시간버렸다..

핵심 아이디어:
1번 문제의 답은 2중 for문을 돌 때 bfs함수의 실행 횟수를 세면 된다.
2번 문제의 답은 영역의 넓이를 구하면서 최대값을 갱신해주면 된다.
3번 문제를 풀기 위해서 우선 bfs, 또는 dfs로 탐색을 하면서 영역을 칠한다.
칠한것은 visited[][][0]에 표시한다.
이후 벽을 만나면 반드시 bfs2로 탐색하며 탐색한 영역의 넓이를 알아낸다.
bfs2는 visited[][][1]에 표시한다.
bfs2로 탐색시 기존의 영역과 만나게 되면 한개의 영역이므로 영역의 넓이는 0을 리턴해 준다.
결과적으로 뚫을수 있는 벽은 1개만 뚫리게 되며 이미 뚫어서 방문한 영역은 다시 계산할 필요 없으므로
----------------------------------------------------------------------------------------
여기서 틀린 예제 추가해야 됨
아래의 논리는 결론적으로 틀림

7 5
3 6 3 2 6 3 6
1 12 9 8 12 1 4
13 3 2 6 15 9 12
3 0 0 4 7 11 6
9 8 8 12 9 14 13

결과:
7
11
16 -> 17이 나와야 함
------------------------------------------------------------------------------------------
틀린 논리:

visited[][][1]은 초기화시키지 말아야 한다.(실제로 초기화 시켰더니 틀렸음...)

visited[][][1]초기화시키지 말아야 하는 이유는
그림에서 순서대로  B  D 라고 하면
                A  C  E
첫번째 과정에서 A+B 가 A+C보다 작으므로 최대를 가지는 영역은 A + C가 된다.
이 때 두번째 bfs()문에서 A와 C를 탐색하지 않아도 되는 이유는 이미 최대값 계산이 이루어져서
최대값영역으로 선택이 되지 않았기 때문이다. 즉 B가 A가 C를 공유하는데 B가 A보다 작으므로
굳이 A+B, B+C를 비교할 필요가 없기 때문이다. 만약 A보다 B가 더 컸으면 첫번째 과정에서
최대값의 영역이 A+B가 됐을 것이다.
이런식으로 비교하기 때문에 기존의 이미 계산된 영역을 중복으로 계산할 필요가 없는 것이다.

틀린 반례: A<B<C일 경우 처음에 최대값이 A+C가 되는데 이후 B+C를 계산하는 과정에서 건너뛰므로
답이 B+C가 되야 하는데 A+C가 되버린다.
--------------------------------------------------------------------------------------
                
                
그러면 3번 문제의 답은 기존의 영역의 넓이 + 뚫은 영역의 최대값이 된다.
이중 for문을 통해 맵의 모든 곳을 탐색하면서 최대값을 갱신해주면 된다.

주의사항:
방향벡터 조심하자
bfs구현시에 배열을 큐에 넣고 싶으면 처음에는 다음과 같이 이중 대괄호를 써야 하고
queue.deque([[0,0,0,0]])
이후 while문 안의 for문 에서는 queue.append([0,0,0,0]) 이렇게 대괄호를 1개만 써야 한다.

---------------------------------------------
최종 수정 09/14/18:35
기존의 풀이는 틀렸으므로 다시 풀었다.
먼저 visited를 통하여 방문을 한 다음에 벽에 인접한 모든 영역을 visited2로 방문을 한다.
만약에 bfs2에서 visited와 만나게 되면 벽을 잘못 뚫은것이므로
0을 리턴해주고 visited2를 방문해놨다고 표시한걸 전부 erase()함수를 통하여 False로 바꿔준다
마지막으로 bfs()의 while을 빠져나와서 {방문한 영역의 인덱스(numofRoom): 영역 크기}를 해시에 저장한다
이후 두번째 방문에서는 이미 visited로 칠해진 영역이 있을텐데, 이 경우에는 영역 계산을 미리 해놨으므로
해시에서 바로 불러오면 된다.
'''

from collections import deque
N, M = 0,0
Map = []
visited = []
visited2 = [] # 벽 뚫고 영역 방문할 때 사용
numofRoom = 0
maxRoomArea = 0
maxRoomArea2 = 0
dataHash = {}

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

def bfs2(_y, _x, nr):
    global N, M, visited2, Map
    
    roomArea = 0
    
    q = deque([[_y, _x]])
    visited2[_y][_x] = True
    
    while q:
        y, x = q.popleft()
        wall = isWall(Map[y][x])
        roomArea += 1
        
        if visited[y][x][1]==nr:
            erase(y,x)
            return 0
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny == M or nx == N:
                continue
            if not visited2[ny][nx] and not wall[i]:
                visited2[ny][nx] = True
                q.append([ny, nx])
    
    return roomArea

def erase(_y, _x):
    global Map, visited2
    
    tmp = [[False for _ in range(N)] for _ in range(M)]
    q = deque([[_y, _x]])
    tmp[_y][_x] = True
    
    while q:
        y, x = q.popleft()
        visited2[y][x] = False
        wall = isWall(Map[y][x])
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny == M or nx == N:
                continue
            if not tmp[ny][nx] and not wall[i]:
                tmp[ny][nx] = True
                q.append([ny, nx])
    
def bfs(_y, _x):
    global N, M, visited, visited2, Map, dataHash, numofRoom
    visited2 = [[False for _ in range(N)] for _ in range(M)]
    roomArea = 0
    roomArea2 = 0
    
    q = deque([[_y, _x]])
    visited[_y][_x][0] = True
    visited[_y][_x][1] = numofRoom
    
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
                if not visited2[ny][nx]:
                    if visited[ny][nx][0]:
                        if visited[ny][nx][1] != numofRoom: #0자 모양 방지하기 위함
                            roomArea2 = max(roomArea2,dataHash[visited[ny][nx][1]])
                    else:
                        roomArea2 = max(bfs2(ny,nx,numofRoom),roomArea2)
                
            else:
                if not visited[ny][nx][0]:
                    visited[ny][nx][0] = True
                    visited[ny][nx][1] = numofRoom
                    q.append([ny,nx])
    
    dataHash[numofRoom]=roomArea
    return roomArea, roomArea2            

if __name__ == "__main__":
    N, M = map(int,input().split())
    for _ in range(M):
        Map.append(list(map(int,input().split())))
    visited = [[[False, -1] for _ in range(N)] for _ in range(M)]
    visited2 = [[False for _ in range(N)] for _ in range(M)]
    
    for y in range(M):
        for x in range(N):
            if not visited[y][x][0]:
                numofRoom += 1
                roomArea, roomArea2 = bfs(y,x)
                maxRoomArea = max(maxRoomArea, roomArea)
                maxRoomArea2 = max(maxRoomArea2, roomArea + roomArea2)
    
    print(numofRoom)
    print(maxRoomArea)
    print(maxRoomArea2)
    
                
    
    