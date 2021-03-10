# 가장 긴 증가하는 부분 수열 4 (https://www.acmicpc.net/problem/14002 )
'''
이진 탐색 아닌 'dp'로 풀어 배열을 리턴할 수 있게 하였음
'''

n = int(input())  # 수열 a 의 길이
a = list(map(int, input().split()))
count_num = [1 for _ in range(len(a))]
answer = []
for i in range(len(a)):
    for j in range(i):
        if a[i] > a[j]:
            count_num[i] = max(count_num[i], count_num[j] + 1)
print(max(count_num))

order = max(count_num)
lst = []
for i in range(n - 1, -1, -1):
    if count_num[i] == order:
        lst.append(a[i])
        order -= 1
lst.reverse()
for i in lst:
    print(i, end=' ')



