#  자신이 구매했던 로또로 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어 졌습니다.
# 알아볼 수 없는 번호를 0으로 표기하기로 하고, 민우가 구매한 로또 번호 6개가 44, 1, 0, 0, 31 25라고 가정해보겠습니다.
#  당첨 번호 6개가 31, 10, 45, 1, 6, 19라면, 당첨 가능한 최고 순위와 최저 순위의 한 예는 아래와 같습니다.
# 순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정됩니다.

# 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수

def solution(lottos, win_nums):
    answer = []
    dic = dict()
    dic[0] = 6
    dic[1] = 6
    for i in range(2,7):
        dic[i] = 7-i
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt+=1
    answer.append(dic[cnt+lottos.count(0)])
    answer.append(dic[cnt])
    return answer

win_nums = [31, 10, 45, 1, 6, 19]
lottos = [44, 1, 0, 0, 31, 25]
# result [5,1]

print(solution(lottos,win_nums))

