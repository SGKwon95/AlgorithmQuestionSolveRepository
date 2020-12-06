'''
중량제한
- https://www.acmicpc.net/problem/1939
- 문제 유형 : BFS, 이분 탐색
- 시간복잡도 = O(N log C) : O(N)은 BFS의 시간복잡도이고 log C는 이분탐색의 시간복잡도 이다.
- 풀이 과정:
    - 모든 간선 내의 최소, 최대 중량을 구하고 그것을 start, end로 초기화한다.
    - 출발지에서 도착지까지 start의 중량으로 bfs 탐색이 가능한지 결정한다.
    - 이것이 가능하면 start를 증가시키고 불가능하면 end를 감소시킨다.
    - start와 end가 일치할 때 까지 이분탐색을 실행한다.
'''
import sys
from collections import deque
def bfs(weight): # start에서 end로 weight 중량으로 갈 수 있는지 체크한다.
    queue = deque([fac_start])
    visited = [False] * (N+1)
    visited[fac_start] = True
    while queue:
        _from = queue.popleft()
        for to, w in graph[_from]:
            if not visited[to] and w >= weight:
                visited[to] = True
                queue.append(to)
    
    return visited[fac_end]

if __name__ == "__main__":
    
    N, M = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    start = int(1e9)
    end = 1

    for _ in range(M):
        a,b,w = map(int,sys.stdin.readline().split())
        graph[a].append((b,w))
        graph[b].append((a,w))
        start = min(start,w)
        end = max(end,w)
        
    fac_start, fac_end = map(int,sys.stdin.readline().split())

    result = start
    while start <= end:
        mid = (start+end) // 2
        if bfs(mid): # 최소와 최대의 중간 weight으로 이동할 수 있으면 weight을 늘려야 하므로 start를 이동시킨다.
            result = mid
            start = mid + 1
        else: # 최소와 최대의 중간 weight으로 이동할 수 없으면 weight을 줄여야 하므로 end를 이동시킨다.
            end = mid - 1
    
    print(result)