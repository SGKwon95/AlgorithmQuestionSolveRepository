# 말이 되고 싶은 원숭이
from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
ndx, ndy = [-2, -2, -1, -1, 2, 2, 1, 1], [1, -1, 2, -2, 1, -1, 2, -2]

# 예제 입력 -------------------------------------
K = int(input())
W, H = map(int, input().split())
Map = []
for i in range(H):
    tmp = list(map(int, input().split()))
    Map.append(tmp)
# -----------------------------------------------

visited = [[[False]*(K+1) for _ in range(W)] for _ in range(H)]
destination = [H-1, W-1]


def bfs():
    answer = -1
    q = deque([[0, 0, 0, 0]])
    visited[0][0][0] = True
    while q:
        y, x, n, d = q.popleft()  # y, x, 말로 이동한 횟수, 동작 횟수
        if [y, x] == destination:
            answer = d
            break

        if n < K:  # 말로 방문할 수 있으면 말로 방문하기
            for i in range(8):
                ny = y + ndy[i]
                nx = x + ndx[i]
                if nx < 0 or ny < 0 or nx >= W or ny >= H or Map[ny][nx] == 1 or visited[ny][nx][n+1]:
                    continue
                visited[ny][nx][n+1] = True
                q.append([ny, nx, n+1, d+1])

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or ny < 0 or nx >= W or ny >= H or Map[ny][nx] == 1 or visited[ny][nx][n]:
                continue
            visited[ny][nx][n] = True
            q.append([ny, nx, n, d+1])

    return answer


print(bfs())
