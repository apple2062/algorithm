#1009 (분산 처리)
# 데이터 개수는 항상 a의b승 개의 형태
# 마지막 데이터가 처리될 컴퓨터의 번호
# 헤맨 부분: (a**b)%10 == 0 일 때를 생각 못해주고 바로 case.append(i) 로 해버리는 바람에 ,
# 컴퓨터번호 10 이 아닌 컴퓨터번호 0 으로 append 되어서 자꾸 틀렸음 ㅋㅋㅋ
t = int(input())
case = []
for i in range(t):
    a,b = map(int,input().split())
    if b%4 == 0:
        b = 4
    else:
        b %= 4
    if (a**b)%10 == 0:
        case.append(10)
    else:
        case.append((a**b)%10)

for i in case:
    print(i)

