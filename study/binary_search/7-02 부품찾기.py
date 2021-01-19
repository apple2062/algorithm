# 부품 찾기
# 시간 복잡도 : O(M * logN)

def binary_search(matrix,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if matrix[mid] == target:
            return mid
        elif matrix[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

n = int(input()) # 부품의 개수
matrix_n = sorted(list(map(int,input().split()))) # 부품 번호 리스트 입력 받고 정렬
m = int(input()) # 대량 구매할 부품의 개수
matrix_m = list(map(int,input().split())) # 구매할 부품 번호 리스트
start , end = 0, len(matrix_n)

for i in matrix_m:
    answer = binary_search(matrix_n,i,start,end)
    if answer != None:
        print("yes",end= ' ')
    else:
        print("no",end = ' ')

