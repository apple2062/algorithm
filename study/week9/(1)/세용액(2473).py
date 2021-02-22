# 세 용액

# 특성값이 0에 가장 가까운 용액을 만들려고 한다.
# 출력해야하는 세 용액은 특성값의 오름차순으로 출력한다

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))  # -2 6 -97 -6 98
lst.sort()

min_ = sys.maxsize
a,b,c = 0,0,0

for i in range(n-2):
    start,end = i+1, n-1
    while start < end:
        sum = lst[i] + lst[end] + lst[start]
        if abs(sum) < min_ :
            min_ = abs(sum)
            a,b,c = lst[i],lst[start],lst[end]
        if sum < 0 :
            start += 1
        elif sum > 0:
            end -= 1
        else:
            print(f'{lst[i]} {lst[start]} {lst[end]}')
            sys.exit(0)

for i in range(3):
    print(f'{lst[a]} {lst[b]} {lst[c]}')



