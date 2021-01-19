# 27. 정렬된 배열에서 특정 수의 개수 구하기
# 시간복잡도 : O(log N)


# x 가 등장하는 횟수를 계산 (단, O(log N) 으로 설계하지 않으면 tle 판정이다)

from bisect import bisect_left,bisect_right

n , x= map(int,input().split()) # 원소의 개수, 출력할 원소
matrix = sorted(list(map(int,input().split())))
answer = bisect_right(matrix,x)-bisect_left(matrix,x)
if answer == 0:
    print(-1)
else:
    print(answer)






