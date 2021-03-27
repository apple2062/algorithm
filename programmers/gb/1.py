# 1.

'''

팩토리얼은 자연수 n에 대해 1부터 n까지 모든 숫자를 곱하는 것을 의미하며 n 팩토리얼은 n! 라고 표기합니다. 예를들어 3! 은 1 x 2 x 3 = 6입니다.
그리고 n! 을 계산했을 때 가장 낮은 자리부터 연속되어 나타나는 0의 개수를 팩토리얼 꼬리의 길이라고 합니다.
예를 들어 n = 10인 경우 10! 은 3628800이며 가장 낮은 자리부터 연속해서 2개의 0이 있으므로 팩토리얼 꼬리의 길이는 2입니다.

입력으로 n이 주어질 때 팩토리얼 꼬리의 길이를 반환하는 함수를 완성해 주세요.

제한사항
n은 231 - 1 이하의 자연수입니다.
'''

def solution(n):
    temp = 5
    answer = 0
    while True:
        answer += n//temp
        if(temp*5 <= n):
            temp *= 5
        else:
            break
    return answer

n = 5 # return 1
# n = 10 # return 2


