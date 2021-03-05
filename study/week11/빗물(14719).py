# 빗물 ( https://www.acmicpc.net/problem/14719 )
'''
1.taregt이라고 둔 높이마다 순회하면서
2.벽 발견 시(target 과 값이 크거나 같은 경우)  그때부터 카운트 1 해준다
3.최초 벽 다음으로 벽을 발견하면 카운트 갱신해주고
    4. 만일 최초 벽 다음으로 벽을 발견하지 못한다면 카운트는 갱신하지 않고 0으로 초기화
'''
# 고이는 빗물의 총량

h,w = map(int,input().split()) #세로, 가로
matrix = list(map(int,input().split())) # [3,1,2,3,4,1,1,2]

rain = 0 # 빗물의 총량

for target in range(h,0,-1):
    lst = [0]*(w)
    lst1 = []
    cnt = 0
    for i in range(w):
        if target<=matrix[i]:
            lst[i] = 1
            lst1.append(i+1)
    if len(lst1)!= 1:
        for i in range(len(lst1)-1):
            cnt += (lst1[i+1]-lst1[i]-1)
    rain+=cnt
print(rain)








