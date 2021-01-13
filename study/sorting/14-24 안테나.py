# 안테나

#특정 위치의 집에 특별히 한 개의 안테나를 설치 , 안테나로부터 모든 집까지의 거리의 총 합이 최소가 되도록 설치
#논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능

import sys
n = int(input()) # 집의 수
matrix = list(map(int,input().split())) #집의 위치
minimum = sys.maxsize
house = 0

for i in range(n):
    answer = 0
    for j in matrix:
        answer += abs(matrix[i]-j)
    if minimum > answer :
        minimum = answer
        house = matrix[i]
        
print(house)
