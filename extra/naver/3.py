# 비싸-싼 <= d 면, 평균으로 판매가 
# 아니면, 비싸 와 싼 을 제외시키고 나머지 중, 비싸-싼<=d 면, 1과 같이 평균값으로 판매가
# prices에서 임의의 k개 골랐을 때, 비싸-싼 <=d 면, k 개의 평균값으로 판매가 결정. 이때, k개 고르는게 여러개라면, 평균값이 가장 낮은 것으로 판매가 결정
# 중앙값을 판매가로 결정. prices오름차순 시, 가운데 위치하는 가격을 판매가로. 이때, 가격개수 짝수개면 둘 중 작은 가격을 판매가로
from collections import deque
from itertools import combinations
def comparing(arr):
    arr.popleft()
    arr.pop()
    return arr
def solution(prices, d, k):
    answer = 0
    prices.sort()
    q = deque(prices)
    while len(q)>1:
        # 조건1
        if abs(q[0]-q[-1]) <= d:
            answer = sum(q)//len(q)
            return answer
        # 조건2
        elif abs(q[0]-q[-1]) > d:
            q = comparing(q)
    #조건 3
    for i in combinations(prices,k):
        if abs(i[0]-i[-1]) <= d:
            return sum(i)//k
    #조건 4
    target = (len(prices)-1)//2
    return prices[target]:
