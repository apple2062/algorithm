# 18 괄호변환

# '(' 의 개수와 ')' 의 개수가 같다면 이를 균형잡힌 괄호 문자열
# '('와 ')'의 괄호의 짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열
# 입력이 빈 문자열인 경우, 빈 문자열을 반환
# 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행
#      수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.



# 올바른 문자열인지 확인하기 위한 함수
def check(p):
    left = 0 #(
    right = 0 #)
    for i in p:
        if i == '(':
            left += 1
        else:
            right += 1
        # 올바르기 위해선 항상 left 가 right 보다 크거나 같아야 하므로
        if left<right:
            return False
    return True

def u_not_right(u,v):
    # 이미 v는 올바른 문자열로 반환되어 들어온 상태
    s = '('
    s += (v+')')
    for i in range(1, len(u)-1):
        if u[i] == '(':
            s+=')'
        else:
            s+='('
    return s

def divide(p):
    # p 가 빈 문자열일 경우
    if p == '':
        return ''
    left = 0  #(
    right = 0 #)
    last = ''

    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        last = p[i]
        if left == right:
            # left와 right의 수가 동일한 상황에서 끝이 right 라면 올바른 문자열임
            if last == ')':
                # u는 올바른 문자열이고, 그 뒤도 재귀적으로 진행
                return p[:i+1] + divide(p[i+1:])
            else:
                return u_not_right(p[:i+1],divide(p[i+1 : ]))



def solution(p):
    # 올바른 문자열인지 확인
    if check(p):
        return p
    return divide(p)
