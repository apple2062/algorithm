# 수 묶기 ( https://www.acmicpc.net/problem/1744 )
'''
풀이 방법 : 그리디로 풀었음
첫 풀이 시 실패한 반례 : 1과 n을 합쳐야 하는 경우, 곱하는 것보다 더하는게 크다는 것을 간과했다.
5
1
1
1
1
1
>> return 5 ( 내 답은 3 이었음)
'''

n = int(input()) # 수열의 크기
minus ,plus = [],[]
answer = 0

for _ in range(n):
    n = int(input())
    if n<0:
        minus.append(n)
    else:
        plus.append(n)
minus.sort() # 음수 배열
plus.sort()  # 양수 배열 (0이 있다면 0도 포함)

while len(plus) > 1:
    x = plus.pop()
    y = plus.pop()
    # 합치는 수 중에 1 이 하나라도 있다면, 곱하지 않고 더해줌
    if x == 1 or y == 1:
        answer += (x+y)
    else:
        answer += (x*y)
while len(minus) > 1:
    answer += (minus.pop(0) * minus.pop(0))

if len(minus) == 1:
    if len(plus)==1:
        if plus[0] != 0:
            answer += (minus.pop() + plus.pop())
    else:
        answer += minus.pop()
else:
    if len(plus) == 1:
        answer += plus.pop()
print(answer)

