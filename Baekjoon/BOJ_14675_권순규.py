import sys
from copy import deepcopy

def dfs(start,root):
    global num
    
    order[start] = num
    num += 1
    
    for i in tree[start]:
        if not order[i]:
            tmp = dfs(i,False)
            
            if not root and order[start] <= tmp:
                cut_vertex[start] = True
            order[start] = min(order[start],tmp)
            
        else: # 이미 방문했으면 그 방문한 노드의 방문순서를 가져온다
            order[start] = min(order[start],order[i])
            
    return order[start]

def dfs2(start,parent):
    global num
    
    order2[start] = num
    num += 1
    
    for i in tree[start]:
        if i == parent:
            continue
        
        if not order2[i]:
            tmp = dfs2(i,start)
            
            if order2[start] < tmp:
                bridge[min(start,i)][max(start,i)] = True
            order2[start] = min(order2[start],tmp)
            
        else: # 이미 방문했으면 그 방문한 노드의 방문순서를 가져온다
            order2[start] = min(order2[start],order2[i])
            
    return order2[start]

if __name__ == "__main__":
    N = int(input())
    tree = [[] for _ in range(N+1)]
    vertexes = [[]]
    cut_vertex = [False] * (N+1)
    bridge = [[False] * (N) for _ in range(N)]
    
    order = [0]*(N+1)
    num = 1
    root = -1
    
    for i in range(1,N):
        a,b = map(int,sys.stdin.readline().split())
        if i == 1:
            root = a
        tree[a].append(b)
        tree[b].append(a)
        vertexes.append((min(a,b),max(a,b)))
            
    if len(tree[root]) >= 2:
        cut_vertex[root] = True
    dfs(root,True)
    
    order2 = deepcopy(order)
    num = 0
    dfs2(root,-1)
    
    q = int(input())
    for _ in range(q):
        t, k = map(int,sys.stdin.readline().split())
        if t == 1:
            if cut_vertex[k]:
                print('yes')
            else:
                print('no')
        else: # t == 2?
            if bridge[vertexes[k][0]][vertexes[k][1]]:
                print('yes')
            else:
                print('no')