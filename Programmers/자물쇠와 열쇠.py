from copy import deepcopy
def rotate(key):
    M = len(key)
    arr = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            arr[j][M-1-i] = key[i][j]
    
    return arr

def isTrue(key,_lock,M,N,sy,sx):
    lock = deepcopy(_lock)
    
    for y in range(M):
        for x in range(M):
            lock[y+sy][x+sx] += key[y][x]
            
    for y in range(M-1,M-1+N):
        for x in range(M-1,M-1+N):
            if lock[y][x] != 1:
                return False
        
    return True


def solution(key, _lock):
    M = len(key)
    N = len(_lock)
    lock = []
    
    for _ in range(M-1):
        lock.append([0]*(N+2*M-2))
    
    for i in _lock:
        lock.append([0]*(M-1)+i+[0]*(M-1))
        
    for _ in range(M-1):
        lock.append([0]*(N+2*M-2))
        
    #for i in lock:
    #    print(i)
    
    for _ in range(4):
        key = rotate(key)
        for y in range(N+M-1):
            for x in range(N+M-1):
                if isTrue(key,lock,M,N,y,x):    
                    return True
    
    return False
    

key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]
print(solution(key,lock))

