# 컵라면 ( https://www.acmicpc.net/problem/1781 )

# 문제를 푸는데는 단위 시간 1이 걸리며, 각 문제의 데드라인은 N이하의 자연수
# 문제는 동호가 받을 수 있는 최대 컵라면 수를 구하는 것
'''
문제번호는 고려하지 않아도 되는 사항.
데드라인으로 정렬해서 라면의 최댓값인 녀석들을 더해가며 값을 갱신하면 될 것같음.

테케:
7
1 9
1 100
2 300
2 99
3 100
5 100
5 999
>> 1599
'''
import heapq

def solution(info):
    q = []
    for i in info:
        # q에 라면 개수 push
        heapq.heappush(q,i[1])
        # q의 길이가 데드라인보다 길어진다면 (=데드라인을 넘어가게 되는 순간이 오면)
        if i[0] < len(q):
            # min heap 성질을 활용해 라면 개수 가장 작은 원소 pop해버림
            heapq.heappop(q)
n = int(input()) #숙제의 개수
info = []
for i in range(n):
    dead , ramen = map(int,input().split())
    info.append((dead,ramen))
info.sort()
print(solution(info))
