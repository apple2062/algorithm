# 빗물 ( https://www.acmicpc.net/problem/14719 )
'''
1.taregt이라고 둔 기준 높이마다 순회하면
2.벽 발견 시(target 과 값이 크거나 같은 경우) 벽 인덱스를 lst에 저장해준다.
3.lst 길이가 1이상인 경우, 저장한 인덱스를 순회하며 인덱스 차이만큼 값을 더해준다.
'''
# 고이는 빗물의 총량

h,w = map(int,input().split()) #세로, 가로
matrix = list(map(int,input().split())) # [3,1,2,3,4,1,1,2]

rain = 0 # 빗물의 총량

for target in range(h,0,-1):
    lst = [] # target보다 높이가 같거나 큰 벽을 만난 경우, 해당 벽의 인덱스를 저장하기 위함
    cnt = 0
    for i in range(w):
        if target<=matrix[i]:
            lst.append(i)
    if len(lst)!= 1: #lst의 길이가 1 이면, 빗물을 감쌀 수 없기 때문에 배제
        for i in range(len(lst)-1):
            cnt += (lst[i+1]-lst[i]-1)
    rain+=cnt
print(rain)







