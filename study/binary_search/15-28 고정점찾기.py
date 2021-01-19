# 28. 고정점 찾기
'''
시간제한 1초, 배열의 길이 100만 까지 가능하다는 것으로 이진 탐색 접근을 떠올렸다.
원소가 오름 차순으로 정렬되어 있으니, mid(:인덱스) 와 value[mid](:값) 비교하여 탐색했다.
'''
# 고정점 : value ==  value[index]
import sys
input_ = sys.stdin.readline().rstrip()

n = int(input_)
matrix = sorted(list(map(int,input().split())))
start,end = 0,n

while start<=end:
    mid = (start+end)//2
    if mid == matrix[mid]:
        print(mid)
        break
    # 인덱스보다 값이 큰 경우
    elif mid > matrix[mid]:
        start = mid +1
    # 인덱스보다 값이 작은 경우
    else:
        end = mid-1

print(-1)




