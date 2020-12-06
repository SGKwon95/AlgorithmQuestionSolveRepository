S = input()
stack = []
ppap = 'PPAP'
for i in S:
    stack += i
    if stack[-1] == 'P' and len(stack) >= 4:
        flag = True
        for j in range(-1,-4-1,-1):
            if stack[j] != ppap[j]:
                flag = False
                break
            
        if flag:
            for _ in range(3):
                stack.pop()
                
if len(stack) == 1 and stack[0] == 'P':
    print('PPAP')
else:
    print('NP')