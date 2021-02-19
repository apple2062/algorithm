# [G3] 드래곤 앤 던전
'''
이진탐색..
'''

# sol 1)
import sys
input = sys.stdin.readline

n,atk = map(int,input().split()) # 방의 개수, 초기 공격력
info = [[] for _ in range(n)]
maxHP, curHP, damage = 0,0,0
for i in range(n):
    t,a,h = map(int,input().split())  # t=1, 몬스터 공격력 a 몬스터 생명력 h / t=2, 용사 공격력 a 증가 용사 생명력 h 회복
    # 용이 있는 방
    if t == 1:
        tmp = h % atk
        if tmp == 0:
            damage = -((h//atk -1) * a)
        else:
            damage = -((h//atk) * a)
    # 포션이 있는 방
    else:
        damage = h
        atk += a
    curHP += damage
    if curHP > 0 :
        curHP = 0
    maxHP = max(maxHP, abs(curHP))
print(maxHP+1)






#sol 2)
T, A, H = [],[],[]
n,atk = map(int,input().split())

for _ range(n):
    t,a,h = map(int,input().split())
    T.append(t)
    A.append(a)
    H.append(h)
start = 1
end = int(1e9)
answer = int(1e9)
while start<end:
    mid = (start+end)//2
    damage = mid
    state = True
    for t,a,h in zip(T,A,H):
        if t==1:
            damage -= ((h-1)//atk)*a
            if damage <= 0:
                state = False
                break
        else:
            atk += a
            damage = min(damage + h, mid)
    if state:
        answer = min(answer,mid)
        end = mid -1
    else:
        start = mid+1
print(answer)











'''
import sys
from math import ceil
input = sys.stdin.readline

def binary_search(start,end,atk):
    while start < end:
        mid = (start+end)//2 #maxhp(최대생명력) 을 나타냄
        max_hp = mid
        for i in info:
            # 용을 만났다면
            if i[0] == 1:
                mid -= (ceil(i[2]/atk)*i[1])
                print("mid" , mid)
            elif i[0] == 2:
                atk += i[1]
                mid += i[2]
                if mid > max_hp:
                    mid = max_hp
                print("atk,mid",(atk,mid))
        break
        if mid > 0 :
            start = mid+1
        else:
            end = mid - 1
    return (start,end)


n,atk = map(int,input().split()) # 방의 개수, 초기 공격력
info = []
maxhp = sys.maxsize
for i in range(n):
    t,a,h = map(int,input().split())  # t=1, 몬스터 공격력 a 몬스터 생명력 h / t=2, 용사 공격력 a 증가 용사 생명력 h 회복
    info.append((t,a,h))

print(binary_search(1,maxhp,atk)) 
'''
