# 안테나
# 시간 복잡도 O(N log N)
'''
첫 시도 시간초과로 실패 
해결 포인트 : 중간값에 해당하는 위치의 집에 안테나를 설치했을 때, 거리 총합이 최소가 된다는 점
'''

n = int(input()) # 집의 수
matrix = list(map(int,input().split())) #집의 위치
matrix.sort()
print(matrix[(n-1)//2])

