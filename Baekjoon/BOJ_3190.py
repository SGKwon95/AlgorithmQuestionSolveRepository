# 뱀
import sys
sys.setrecursionlimit(12000) # 이거 안걸면 런타임 에러 남

#런타임 종류:
# 배열 인덱스 벗어난 경우
# 가능한 재귀 호출 값을 넘어간 경우

dx, dy = [1,0,-1,0],[0,1,0,-1] #동남서북

current = 0

def pr():
    print()
    for i in Map:
        print(i)



def move(y,x,ty,tx,answer,direction):
    global current
    
    eat = False
    if y < 0 or x < 0 or y == N or x == N:
        print(answer)
        sys.exit(0)
    
    if Map[y][x] == 2: # 자기 몸이면 종료
        print(answer)
        sys.exit(0)
        
    if Map[y][x] == 1: # 사과이면
        eat = True
    
    if [y,x] == [0,0]:
        eat = True
    
    Map[y][x] = 2
    Dir[y][x] = direction
    #pr()
    #print('eat=',eat,'answer=',answer)
    
    if answer == go[current][0]:
        
        if go[current][1] == 'D':
            Dir[y][x] += 1
            if Dir[y][x] == 4:
                Dir[y][x] = 0
        
        else:
            Dir[y][x] -= 1
            if Dir[y][x] < 0:
                Dir[y][x] = 3
                
        if current < numofgo-1:
            current += 1
            
        if not eat:
            Map[ty][tx] = 0 
            move(y+dy[Dir[y][x]],x+dx[Dir[y][x]],ty+dy[Dir[ty][tx]],tx+dx[Dir[ty][tx]],answer+1,Dir[y][x])
        else:
            move(y+dy[Dir[y][x]],x+dx[Dir[y][x]],ty,tx,answer+1,Dir[y][x])
            
    else:
        if not eat:
            Map[ty][tx] = 0 
            move(y+dy[Dir[y][x]],x+dx[Dir[y][x]],ty+dy[Dir[ty][tx]],tx+dx[Dir[ty][tx]],answer+1,Dir[y][x])
        else:
            move(y+dy[Dir[y][x]],x+dx[Dir[y][x]],ty,tx,answer+1,Dir[y][x])
    
        
    

if __name__ == "__main__":
    N = int(input())
    Map = [[0] * N for _ in range(N)]
    Dir = [[0] * N for _ in range(N)]
    
    K = int(input())    
    for _ in range(K):
        y, x = map(int,input().split())
        Map[y-1][x-1] = 1
    
    L = int(input())
    go = []
    for _ in range(L):
        X, C = input().split()
        go.append([int(X),C])
    numofgo = len(go)
    
    move(0,0,0,0,0,0)