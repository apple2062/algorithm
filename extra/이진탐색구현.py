def binary(array,target,start,end):
    while start <= end :
        mid = (start+end)//2
        # 바로 찾은 경우
        if array[mid] == target:
            return mid
        # 중간점보다 타겟 값이 작은 경우
        elif array[mid] > target:
            end = mid-1
        # 중간점보다 타켓 값이 큰 경우
        else:
            start = mid + 1

array,target,start,end = [1,3,5,7,7,7,9,11,13,15,17,19], 7, 0, len(array)
result = binary(array, target, start, end)
