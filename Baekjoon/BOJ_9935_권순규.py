text = input()
bombstr = input()
bl = len(bombstr)
answer = []

for ch in text:
    answer.append(ch)
    if bombstr[-1] == answer[-1] and len(answer) >= bl:
        flag = True
        for j in range(-2,-bl-1,-1): # 파이썬만 쓸 수 있는 사기 스킬
            if answer[j] != bombstr[j]:
                flag = False
                break
        
        if flag:
            for i in range(bl):
                answer.pop()

if not len(answer):
    print('FRULA')
else:
    for i in answer:
        print(i,end='')