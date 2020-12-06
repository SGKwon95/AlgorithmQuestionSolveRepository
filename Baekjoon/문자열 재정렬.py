S = input()
num = 0
character = []
for i in S:
    if 0 <= (ord(i)-ord('0')) <= 9:
        num += (ord(i)-ord('0'))
    else:
        character.append(i)
character.sort()
for ch in character:
    print(ch,end='')
print(num)