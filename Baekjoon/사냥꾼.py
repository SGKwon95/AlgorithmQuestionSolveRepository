import sys
M,N,L = map(int,sys.stdin.readline().split())
places = list(map(int,sys.stdin.readline().split()))
animals = []
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    animals.append((y,x))