'''
     1)1초 간격으로 바이러스들이 집 안으로 침입한다
     2) 집 안에서 바이러스는 1초당 P배씩 증가한다
     3) N초 동안 죽는 바이러스는 없다

     매초 집 안에 침입하는 바이러스의 숫자가 주어질 때, N초 후에는 총 몇 마리의 바이러스를 잡아야 할까?
     최종 바이러스 개수를 1000000007로 나눈 나머지를 출력
'''
def solution(p,n,virus):
    answer = 0
    target = n-1
    for i in virus:
        val = i*(p**(target))
        answer += val
        target -= 1
    return answer%1000000007

p, n = map(int,input().split()) #증가율, 총 시간
lst = list(map(int,input().split())) # 매 초 침입하는 바이러스의 숫자
print(solution(p,n,lst))

'''
3 3
1 2 3
>> 18
'''
