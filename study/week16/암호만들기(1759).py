# 암호 만들기 ( https://www.acmicpc.net/problem/1759 )

'''
30% 대에서 자꾸 틀렸습니다 떠서 고생했다
>> l = 3 c=7 인 경우, length = l-i 로만 둬버리면 length 가 음수  또는 1인 경우도 포함되기 떄문에
    이를 제외시켜주어야 함. 그래서 length < 2 인 경우는 break 거는 조건문을 추가했음
'''

from itertools import combinations
def solution(alp):
    answer = set()
    zaum = []
    moum = []
    for i in alp:
        if i in ['a','e','i','o','u']:
            moum.append(i)
        else:
            zaum.append(i)
    for i in range(1,len(moum)+1):
        for j in combinations(moum,i):
            length = l-i
            # 모음 최소 1개, 자음 최소 2개여야 하는데 length<2 이면 자음이 1개 이하 이므로 해당 조건은 제외시켜주어야함
            if length < 2:
                break
            for k in combinations(zaum,length):
                lst = sorted(list(j) + list(k))
                str = ''.join(lst)
                answer.add(str)
    return sorted(list(answer))

l,c = map(int,input().split()) # 암호는 서로 다른 L개의 알파벳 소문자들, 암호로 사용했을 법한 문자의 종류
alp = list(input().split())

answer = solution(alp)
for i in answer:
    print(i):
