def calDistance(a,b):
    if abs(a[0]-b[0])+abs(a[1]-b[1]) <= 1000:
        return abs(a[0]-b[0])+abs(a[1]-b[1])
    else:
        return INF
    
def Floyd_Warshall(N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                   dist[i][j] = dist[i][k] + dist[k][j]

import sys
INF = int(1e9)
if __name__ == "__main__":
    for _ in range(int(input())):
        numofConv = int(sys.stdin.readline())
        graph=[]
        visited = [False] * (numofConv+2)
        dist = [[INF] * (numofConv+2) for _ in range(numofConv+2)]
        for i in range(numofConv+2):
            graph.append(tuple(map(int,sys.stdin.readline().split())))
        
        for i in range(numofConv+2):
            for j in range(numofConv+2):
                dist[i][j] = calDistance(graph[i],graph[j])
        
        Floyd_Warshall(numofConv+2)
        if dist[0][numofConv+1] != INF:
            print('happy')
        else:
            print('sad')
        