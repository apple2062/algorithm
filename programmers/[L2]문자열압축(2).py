# 09 문자열 압축
# @@@ 5번 테케 불통했던 반례 : input "a" return 1  @@@

def solution(s):
    min = 1000
    answer = ''
    length = len(s)
    
    # len(s) 가 1일 때, 두번째 for 문 진입을 하지 않으므로 그대로 min=1000 을 return 함을 방지해야함
    if len(s) == 1:
        return 1
    
    for i in range(1,(length//2)+1):
        cnt = 1
        word = s[:i]

        # 문자열을 꼭 2로 나누어 문자열 길이보다 더 넘어가는 비교는 할 필요 없도록 하기
        for j in range(i,len(s),i):
            target = s[j:j+i]
            # 단위로 쪼갠 글자(word)와 비교 대상(target)을 비교
            if target == word:
                cnt += 1
            else:
                # target != word 인 상황에서 중복 된 단어가 없는 경우
                if cnt == 1:
                    cnt = ''
                answer += (str(cnt) + word)
                word = target
                cnt = 1
        #두번째 for문 탈출 후 마지막에 한번 더 answer 에 str(cnt) + word 을 넣어 제일 마지막으로 비교했던 문자열이 들어가게 함
        if cnt == 1:
            cnt = ''
        answer += (str(cnt)+word)
        if len(answer) < min:
            min = len(answer)
        answer = ''
    return min

#s = list(input())
s = "a"  #return 1
print(solution(s))
