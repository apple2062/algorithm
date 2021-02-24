# 스타트 링크 (https://www.acmicpc.net/problem/14889)
'''
첫번째 풀이 : 28776kb메모리	5868ms시간....ㅋㅋㅋ다른 분들 걸린 시간 궁금하다 접근방법이랑
+ set 이용 안하고 푸신 분 있으까??!?!?!?

combination 으로 풀긴 했는데 시간이 엄청 많이 소요되는 것 같다..ㅎ.ㅎ
'''
from itertools import combinations
import sys

def solution(team1,team2):
    power1,power2 = 0,0
    for i in range(n//2):
        for j in range(n//2):
            power1 += matrix[team1[i]-1][team1[j]-1]
            power2 += matrix[team2[i]-1][team2[j]-1]
    return abs(power1-power2)

n = int(input())
member = [i for i in range(1,n+1)]
matrix = [list(map(int,input().split())) for _ in range(n)]
answer = sys.maxsize

for i in combinations(member,n//2):
    team1 = list(i)
    team2 = list(set(member)-set(team1))
    value  = solution(team1,team2)
    answer = min(answer,value)

print(answer)


