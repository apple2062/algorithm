import math
def solution(progresses, speeds):
    days = []
    ans = []
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i])) #[7,3,9] 소요되는 day에 대한 새로운 list 생성

    idx = 0 #함께 배포되는 기능 바로 다음부터 인덱스 취해주기 위해 필요
    cnt = 0
    for i in range(len(days)):
        if days[idx] >= days[i]:
            cnt += 1
        else:
            ans.append(cnt)
            cnt = 1
            idx = i
        if i == len(days)-1: #배열 끝에서 cnt셌던 것을 붙여주기 위함
            ans.append(cnt)
    return ans

#print(solution([93,30,55],[1,30,5]))  #return [2,1]


