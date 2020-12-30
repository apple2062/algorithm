# 08 문자열 재정렬 (O(n))

# 모든 알파벳을 오름차순후 정렬한 후, 그 뒤 모든 숫자를 더한 값을 이어서 출력
def solution(s):
    # 숫자를 담을 배열
    num = []
    # 대문자 담을 배열
    char = []
    for i in s:
        # ord('1') == 49 ~ ord('9') == 57 임을 활용하여 숫자만 걸러냄
        if 49<=ord(i)<=57:
            num.append(int(i))
        else:
            char.append(i)
    s = ''.join(sorted(char,key=lambda x:ord(x)))
    return s+str(sum(num))

s = list(input())
print(solution(s))




