N, A, B = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()

sum = 0
size = 0

if N%2 == 1:
    sum += a[-1]
    size += 1

    
while size < N:
    t1, t2 = 0, 0
    if len(a) >= 2:
        t1 = a[-1] + a[-2]
    if len(b) >= 1:
        t2 = b[-1]
        
    if t1 > t2:
        sum += t1
        a.pop()
        a.pop()
    else:
        sum += t2
        b.pop()
    
    size += 2
        
print(sum)