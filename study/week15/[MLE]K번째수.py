# K번째수 (https://www.acmicpc.net/problem/1300 )
'''
k는 min(109, N2)보다 작거나 같은 자연수 >> 범위 대박 크
'''

def solution(n,k):
    matrix = []
    for i in range(n):
        for j in range(n):
            matrix.append((i+1)*(j+1))
    matrix.sort()
    return matrix[k]

n = int(input()) # 배열의 크기
k = int(input()) # B를 오름차순 정렬한 후 B[k]값

print(solution(n,k))
