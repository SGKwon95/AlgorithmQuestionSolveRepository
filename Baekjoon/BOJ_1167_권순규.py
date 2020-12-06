# 트리의 지름
# 정석대로 풀다가 시간초과 남
import sys

def dfs(start, length):
    
    maxlength[start] = 0
    
    for i in graph[start]:
        if maxlength[i[0]]==0:
            maxlength[start] = max(dfs(i[0],length + i[1]),maxlength[start])
        else:
            maxlength[start] = max(maxlength[start], maxlength[i[0]])
    
    return maxlength[start]
    
    
        

V = int(input())
graph = [[] for _ in range(V+1)]
maxlength = [0 for _ in range(V+1)]
answer = 0
for i in range(1, V+1):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(tmp)-2, 2):
        graph[i].append((tmp[j], tmp[j+1]))
        
print(graph)


for i in range(1, V+1):
    dfs(i,0)
    visited = [False for _ in range(V+1)]

print(answer)