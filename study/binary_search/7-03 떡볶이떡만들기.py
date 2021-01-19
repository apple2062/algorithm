# 떡볶이 떡 만들기
# 시간 복잡도 : O(N *  log N)

'''
첨에 이게 왜 이진 탐색 문제인가 싶었다.
절단기 높이를 계속 조정해가며 조건을 만족하는지 확인하는 문제인데 탐색 범위를 어떻게 좁힌다는 건지 감이 안왔음..
근데 절단기 높이가 최대 10억 정도까지라 보아, 무조건 순차적 탐색으론 tle 뜰 것 같았기에 이진 탐색 아이디어를 생각해 보았다

해결 방안 : 절단기 높이(H)에 대한 이진 탐색. 일단 가장 긴 떡의 길이 범위 내에 있어야 떡을 자를 수 있으므로 end = len(matrix) 로 설정
         그 후 절단기 높이에 대한 이진 탐색 수행 
'''
n, m = map(int, input().split())  # 떡의 개수, 요청한 떡의 길이
matrix = sorted(list(map(int, input().split())))  # 떡의 개별 높이
start, end = 0, max(matrix)

while start <= end:
    H = (start + end) // 2
    length = 0
    for i in matrix:
        if i - H >= 0:
            length += (i - H)
    if length == m:
        print(H)
        break
    # 절단기 높이에 비해 떡의 길이합이 길다면
    elif length > m:
        start = H + 1
    # 절단기 높이에 비해 떡의 길이합이 짧다면
    else:
        end =H - 1

