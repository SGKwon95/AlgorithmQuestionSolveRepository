import sys

def getDistance(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def divide(left,right):
    N = right-left
    if N == 2:
        return getDistance(dots[left],dots[left+1])
    elif N == 3:
        return min(getDistance(dots[left],dots[left+1]),getDistance(dots[left+1],dots[left+2]),getDistance(dots[left+2],dots[left]))

    M = (left + right)//2
    d = min(divide(left,M),divide(M,right)) # 가장 짧은 거리
    
    target = [] # 서로 다른 그룹에서의 두 점에서 최단 거리가 나올 후보를 저장할 리스트
    vs = []
    start = M
    answer = d
    while start < right:
        if dots[start][0] <= dots[M][0] + d:
            target.append(dots[start])
            start += 1
        else:
            break
    
    start = M-1
    while start >= left:
        if dots[start][0] >= dots[M-1][0] - d:
            vs.append(dots[start])
            start -= 1
        else:
            break
    
    for i in target:
        for j in vs:
            answer = min(answer,getDistance(i,j))
    
    return answer
        
    


if __name__ == "__main__":
    n = int(input())
    dots = []
    for _ in range(n):
        dots.append(tuple(map(int,sys.stdin.readline().split())))
    
    if len(set(dots)) != n:
        print(0)
    else:
        dots.sort(key=lambda x:(x[0],x[1]))
        print(divide(0,n))
            