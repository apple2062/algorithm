# 카카오 머니 ( https://www.acmicpc.net/problem/15998)
'''
 조건 잡는게 너무너무 까다로웠다.
 특히 내 코드 반례 테스트 케이스 찾는게 엄청 힘들었다.....
 반례들에 대한 조건 잡다가 한나절 다감.. 못품 ㅋㅋㅋ

 >> 충전이 한 번도 이루어지지 않는 경우서 즉, 후보군 possible 이 생성되지 않은 경우
    -1이 아니라 임의의 양의 정수가 M이 될 수 있다. 이 부분을 놓쳤었........
'''

import sys
from math import gcd

n = int(input())
log = [(0,0)]
possible = []

def get_gcd(possible):
    while True:
        possible.append(gcd(possible.pop(), possible.pop()))
        if len(possible) == 1:
            if possible[0] == 1:
                return -1
            else:
                return possible[0]


for i in range(n):
    a,b = map(int,input().split())
    log.append((a,b))

for i in range(1,n+1):
    if log[i][1] != log[i-1][1] + log[i][0]:
        if i==1 and log[i][0] > 0 :
            continue
        if log[i-1][1] > log[i][1]:
            print("-1")
            sys.exit(0)
        possible.append(log[i][1]-(log[i-1][1] + log[i][0]))

if len(possible) <= 1:
    if len(possible) == 0:
        print("1")
        sys.exit(0)
    print("-1")
    sys.exit(0)

print(get_gcd(possible))


'''
반례 테케
2
1500 1500
-300 1200
>> 1 (임의의 양의 정수가 M이 될 수 있음)

3
1500 1500
-1600 1200
-400 0
>> -1 (3번째 로그에 모순이 있음)
'''
