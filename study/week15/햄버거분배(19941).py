# 햄버거 분배 ( https://www.acmicpc.net/problem/19941 )

import sys
N, K = list(map(int, sys.stdin.readline().split()))
table = sys.stdin.readline().strip()

def solution():
    eat = [0] * N
    answer = 0
    for i in range(N):
        if table[i] == 'P':
            for offset in range(-K, K + 1):
                idx = i + offset
                if 0 <= idx < N and table[idx] == 'H' and not eat[idx]:
                    eat[idx] = 1
                    answer += 1
                    break
    return answer
print(solution())

"""
20 1
HHPHPPHHPPHPPPHPHPHP
>> 8

20 2
HHHHHPPPPPHPHPHPHHHP
>> 7
"""
