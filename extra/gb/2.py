# 2. 문자열 s가 주어질 때 좋은 부분 문자열의 개수를 return 하도록 solution 함수를 완성해주세요.
'''
좋은 부분 문자열이란 어떤 문자열 s의 부분 문자열이면서 같은 알파벳이 두 번 이상 나타나지 않는 문자열을 말합니다.
예를 들어 주어진 문자열이 "abac" 일 때, 부분 문자열 "a", "ab", "bac"등은 원래 문자열 "abac" 의 부분 문자열이면서 문자열 내에 같은 알파벳이 두 번 이상 나타나지 않으므로 좋은 부분 문자열입니다. 그러나 "aba", "abac"는 문자열 내에 같은 알파벳 'a'가 두 번 이상 나타나므로 좋은 부분 문자열이 아닙니다. 문자열 s가 주어질 때 좋은 부분 문자열의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
문자열 s의 길이는 1 이상 100 이하이며, 알파벳 소문자로만 이루어져 있습니다.
여러 번 나타나는 같은 부분 문자열은 하나로 세면 됩니다.
'''
def goodstring(str):
    if len(list(str)) != len(set(str)):
        return False
    return True

def solution(s):
    answer = set()
    start = 0
    end = 1
    while start < len(s):
        if goodstring(s[start:end]):
            answer.add(s[start:end])
            end += 1
        else:
            start += 1
            end = start + 1
        if end > len(s):
            start += 1
            end = start + 1
    return len(answer)

#s = "abac"
s = "abcd"
# s = "zxzxz"
print(solution(s))
