# abcabcdede와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 abcabc2de가 되지만,
# #3개 단위로 자른다면 2abcdede가 되어 3개 단위가 가장 짧은 압축 방법
# "ababcdcdababcdcd"	-> 9
# "abcabcdede" ->	8
# "abcabcabcabcdededededede"->	14
def solution(s):  # 1부터 length/2 까지가 단위(step) 이 됨
    wording = ""
    size = len(s) // 2
    ans = []
    for i in range(6, size + 1):  # 스텝
        part = s[0:i]  # 기준이 될 놈
        cnt = 1
        for j in range(i, len(s), i):  # 스텝만큼 비교하기
            if part == s[j:j + i]:
                cnt += 1
            else:
                wording += part
                if cnt > 1:
                    wording += str(cnt)
                part = s[j:j + i]
                cnt = 1
        wording += part
        if cnt > 1:
            wording += str(cnt)
        ans.append(len(wording))
        print(i, len(wording), wording)
        wording = ""
    return min(ans)

