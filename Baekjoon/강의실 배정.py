'''
https://www.acmicpc.net/problem/11000
강의실 배정
최적의 해 = 최대한 빈 시간이 없도록 해야 함
'''

import sys, heapq
N = int(input())
pq = []
lst = []
pq = []

for _ in range(N):
    lst.append(tuple(map(int,sys.stdin.readline().split())))

lst.sort(key=lambda x:x[0]) # 빨리 시작하는 순서대로 정렬한다.

pq.append(lst[0][1])
                   
for i in range(1,N):
    if pq[0] <= lst[i][0]: # pq[0]은 계속 바뀐다.
        heapq.heappop(pq)
    heapq.heappush(pq,lst[i][1])

# 최종 시간복잡도 = O(N) (반복문) * O(log N) (힙 삽입, 정렬 비용)

print(len(pq))

'''
그러니까 원래 생각대로 pq는 무조건 빨리 끝나는 순서대로 저장해야되는게 맞음
그러면 lst는 무조건 빨리 시작하는 순서대로 정렬해야 함
'''