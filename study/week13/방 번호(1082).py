# 방 번호 ( https://www.acmicpc.net/problem/1082)
'''
미해결.. 그리디로 접근하고자 했다.
1. 일단 최대한 많은 자릿수를 확보해야 하고
2. 맨 앞 숫자가 커야한다.

이 개념으로 접근 했는데, 해결 못했음 ㅠ
'''

# 최대한 많은 자리수를 확보해야 함 > 최대한 많은 숫자를 사기 위해 가장 싼 숫자를 구매
# 가장 큰 자릿수부터 큰 수로 바꿀 수 있는지 (남은돈) 과 (차액) 을 비교

import sys
from collections import deque

def solution(money_, digit):
    print("money_, digit :  ",money_,lst,digit)
    # 가장 큰 오른쪽 숫자부터 가장 큰거 넣어보기
    for i in range(digit, -1, -1):
        # 현재 자릿수가 가장 큰 값이 아니라면
        if lst[i] != n - 1:
            # 큰거부터 넣어봄
            for j in range(n - 1, lst[i], -1):
                nowCost = price[j] - price[lst[i]]
                print(nowCost, price[j], price[lst[i]])
                if nowCost <= money_:
                    lst[i] = j
                    solution(money_ - nowCost, digit - 1)
                    return
    # 모두다 0이면
    if not any(lst):
        if not lst:
            print(0)
            sys.exit()
        lst.pop()
        solution(money + price[0], digit - 1)



n = int(input()) # 문방구에서 파는 숫자의 개수 (n = 4 , [0,1,2,3])
price = list(map(int,input().split()))
money = int(input()) # 현재 가지고 있는 비용

minCost = min(price) #최소 금액
minNum = price.index(minCost) #최소 금액의 인덱스

# 숫자의 개수가 0 하나일 경우
if n==1:
    print(0)
    sys.exit()

num = money // minCost # 가능한 최대 자릿수
lst = [minNum for i in range(num)] # 비용이 가장 작은 놈의 값으로 num길이 만큼의 배열 생성
cost = num * minCost
print(num,lst,cost)


solution(money-cost,num-1)

ans=0
for i in range(len(lst)):
    ans+=(10**i)*lst[i]



