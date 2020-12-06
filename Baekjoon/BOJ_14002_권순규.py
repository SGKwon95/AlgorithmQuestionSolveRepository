# 가장 긴 증가하는 부분 수열4
import sys
N = 0
arr = []
answer = 0
answerArr = []
cache = [-1] * 1000
go = [-1] * 1000

def lis(start): # start에서 시작하는 가장 긴 증가하는 부분 수열의 길이
    global cache
    if cache[start] != -1:
        return cache[start]
    
    cache[start] = 1
    
    for next in range(start+1,N):
        if arr[start] < arr[next]:
            tmp = lis(next) + 1
            if cache[start] < tmp:
                cache[start] = tmp
                go[start] = next
    
    return cache[start]

def cnt(start, n, result):
    #print(n,result)
    if go[start] == -1:
        if n == answer:
            for i in result:
                print(i, end=' ')
            sys.exit(0)
    else:
        cnt(go[start],n+1,result+[arr[go[start]]])

if __name__ == "__main__":    
    N = int(input())
    arr = list(map(int,input().split()))
    for i in range(N):
        answer = max(answer,lis(i))
    
    print(answer)
    
    for i in range(N):
        cnt(i,1,[arr[i]])
    

