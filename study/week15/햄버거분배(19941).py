# 햄버거 분배 ( https://www.acmicpc.net/problem/19941 )

# P(사람)와 H(햄버거)
import sys
input = sys.stdin.readline

def solution():
    answer = 0
    visited = [False]*n
    for i in range(n):
        if info[i] == 'P':
            for j in range(-k,k+1):
                idx = i+j
                if 0<=idx<n and info[idx] == 'H':
                    if not visited[idx]:
                        visited[idx] = True
                        answer += 1
                        break
    return answer

n,k = map(int,input().split())
info = input()

print(solution())


"""
20 1
HHPHPPHHPPHPPPHPHPHP
>> 8

20 2
HHHHHPPPPPHPHPHPHHHP
>> 7
"""
