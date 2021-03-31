# 시험 감독 ( https://www.acmicpc.net/problem/13458 )
'''
총감독관이 어떤 시험장에 있는 응시자 수보다 많은 수를 감시할 수 있는 경우에 대한 처리가 안 되어 있습니다.
1
1
2 1
감독관은 최소 1명 있어야 하지만, 0이 출력됩니다.

관련된 반례 :
2
1 1
2 1 >> answer : 2, 내 답: 0
'''
# 시험장에 총감독관은 오직 1명, 부감독관은 여러명 있어도 됨
# 각 시험장마다 응시생을 모두 감시해야 할때, 필요한 감독관 수의 최솟값

def solution(n,applicant,b,c):
    answer = n
    for i in applicant:
        val = (i-b)
        if val<0:
            continue
        if val%c == 0:
            answer += (i-b)//c
        else:
            answer += ((i-b)//c+1)
    return answer

n = int(input()) #시험장의 개수
applicant = list(map(int,input().split())) #각 시험장에 있는 응시자 수
b,c  = map(int,input().split()) # 총감독관이 한 시험장에서 감시 가능한 응시자수 , 부감독관이 한 시험장에서 감시 가능한 응시자 수

print(solution(n,applicant,b,c))
