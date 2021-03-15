# 지름길 (https://www.acmicpc.net/problem/1446 )
'''
distance[j] = min(distance[j], distance[j - 1] + 1) 해당 코드를
for i in information 로직 다음에 삽입하여 계속 틀렸다. 근데 이게 뭐가 문제인건지 진짜 모르겠음.. 리뷰할 때 물어보기

그 위로 바꿔 넣으니 통과했음.. 왜지

틀렸을 때 반례 :
5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 10
>> 50 (내 답은 70나왔다)
'''
# n 은 12 이하 ,  D는 10,000보다 작거나 같은 자연수
n,d = map(int,input().split()) #지름길의 개수, 고속도로의 길이

information = []
distance = [i for i in range(d+1)] #[0,1,2,3,...,150]

for i in range(n):
    x,y,length = map(int,input().split()) # 지름길의 시작 위치, 도착 위치, 지름길의 길이
    if d >= y :
        information.append([x,y,length]) #[0,50,10], [0,50,20]...

for j in range(d+1):
    distance[j] = min(distance[j], distance[j - 1] + 1)
    for i in information:
        if j == i[0]:
            distance[i[1]] = min(distance[i[1]],distance[i[0]]+i[2])

print(distance[-1])



