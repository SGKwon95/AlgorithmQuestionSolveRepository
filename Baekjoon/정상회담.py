'''
https://www.acmicpc.net/problem/1795
- 문제 이름 : 정상 회담
- 문제 유형 : BFS, 그래프, 구현
- 아이디어:
  - 각 숫자에서 시작해서 BFS를 수행한 다음에 이동횟수를 계산하여 Map에 append한다.
  - 그 다음에 Map의 원소 개수가 숫자 개수만큼 나오면 이는 모두 모인 것이므로 최솟값을 계속 갱신한다.
- 이전에 놓쳤던 내용은 같은 숫자가 여러 번 가능하다는 사실을 고려하지 않아서 틀렸다.
'''

def dfs(num,location):
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[location[0]][location[1]] = True
    Map[location[0]][location[1]].append(0)
    q = deque([[location,0]])
    while q:
        (y,x), t = q.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            
            if not visited[ny][nx]:
                visited[ny][nx] = True
                if (t+1)%num == 0:
                    Map[ny][nx].append((t+1)//num)
                else:
                    Map[ny][nx].append((t+1)//num + 1)
                q.append([(ny,nx),t+1])

from collections import deque
import sys
dx, dy = (1,2,2,1,-1,-2,-2,-1),(2,1,-1,-2,-2,-1,1,2)
if __name__ == "__main__":
    N, M = map(int,input().split())
    Map = [[[] for _ in range(M)] for _ in range(N)]
    startLocation = [[] for _ in range(9)]
    Maal = []
    for y in range(N):
        tmp = input()
        for x in range(M):
            if '1' <= tmp[x] <= '9':
                startLocation[ord(tmp[x])-ord('1')].append((y,x))

    numofMaal = 0
    for i in range(9):
        if startLocation[i]:
            numofMaal += len(startLocation[i])
            for j in startLocation[i]:
                Maal.append((i+1, j))
            
    if numofMaal == 0:
        print(-1)
        sys.exit(0)
    
    for i in Maal:
        dfs(i[0],i[1])
        
    canGather = False
    answer = int(1e9)
    for y in range(N):
        for x in range(M):
            if len(Map[y][x]) == numofMaal:
                canGather = True
                tmp = sum(Map[y][x])
                answer = min(answer,tmp)
    
    if canGather:
        print(answer)
    else:
        print(-1)
                