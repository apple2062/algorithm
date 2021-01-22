# 게임
# 시간 복잡도 : O(M * log N) // M: 탐색 횟수
# z>=99 로 해야 하는 점을 주의해야한다.(첨에 x==y인 경우만을 고려한 z==100으로 두었다가 실패했었음 ㅋㅋㅠㅠ) 
 
'''
x 가 최대 10억인것으로 볼때, x 값이 높으면 높을 수록 z 가 변하기 전까지 하나하나 계산해보기가 tle 초과날 듯 싶었다. (물론 시간초과 났음)
늘릴 판수(n) 에 대한 이진 탐색을 진행해야 될 것 같다.

풀이 방법 : n에 대한 이진 탐색
          start,end = 1,10억으로 선언 후 ,mid 값 n 에 대한 승률(z)이 z 보다 크다면, end = mid-1
          마찬가지로 mid 값 n 에 대한 승률(z)이 z 보다 작다면 start = mid + 1 해주었다.
'''
x,y = map(int,input().split())
z = (100*y) // x
start, end = 1, 1000000000
if z >= 99 :
    print(-1)
    exit(0)
while start <= end:
    mid = (start + end) // 2
    percentage = 100 * (y + mid) // (x + mid)
    if percentage > z:
        end = mid -1
    else:
        start = mid + 1
print(start)

-----------------------------------------------------------------------------------------------------
# 두번 쨰 풀이 - (시간 초과)
import sys,timeit
start_time = timeit.default_timer()  # 시작 시간

x, y = map(int,input().split())
z = (y*100)//x # 승률
cnt = 0
while True:
    if x==y:
        print(-1)
        break
    x += 1
    y += 1
    rate = (y*100)// x
    cnt += 1
    if rate == z + 1:
        print(cnt)
        break
end_time = timeit.default_timer() # 종료시간
print(end_time - start_time)

