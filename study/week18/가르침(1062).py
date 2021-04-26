# 가르침 ( https://www.acmicpc.net/problem/1062 )
# ref :  https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-1062-%EA%B0%80%EB%A5%B4%EC%B9%A8

'''
a/c/i/t/n/을 제외한 알파벳 배열을 2진수 숫자로 만들어주는 함수 word_to_bin을 만든다.
예를 들어, 함수의 입력값이 'bbfxz'라면, 출력값은 0b100100000000000000101이다.
물론 이 함수에 값을 넣기 전에는 미리 a/c/i/t/n/을 없애주어야 한다.

k가 5보다 작다면, 만들 수 있는 단어의 최대 개수는 0이다.

k가 5 이상이라면, a/c/i/t/n/을 제외한 21개의 알파벳 중 k - 5개의 알파벳으로 만들 수 있는 모든 조합에 대하여,
표현할 수 있는 단어의 개수를 구한다. 그 값의 최대값이 정답이 될 것이다.
k - 5개의 알파벳의 조합은 2진수로 표현한다. 예를 들어, ('b', 'd', 'z')라면, 0b101000000000000000001로 표현한다.
'''

from sys import stdin
from itertools import combinations

# a/c/i/t/n을 제외한 알파벳 각각에 고유 번호 부여
bin_dict = {'b': 20, 'd': 19, 'e': 18, 'f': 17, 'g': 16, 'h': 15, 'j': 14,
            'k': 13, 'l': 12, 'm': 11, 'o': 10, 'p': 9, 'q': 8, 'r': 7,
            's': 6, 'u': 5, 'v': 4, 'w': 3, 'x': 2, 'y': 1, 'z': 0}

# 알파벳 배열을 2진수로 바꾸어주는 함수
def word_to_bin(word):
    answer = 0b0
    for x in word:
        answer = answer | (1 << bin_dict[x])
    return answer


n, k = map(int, stdin.readline().split())
words = []
# 각 입력 단어에 대하여
# 1. 앞의 anta와 뒤의 tica를 슬라이스한 뒤 set로 만들고
# 2. 그중 a/c/i/t/n을 제외한 뒤 words 리스트에 저장
for _ in range(n):
    words.append(set(stdin.readline().rstrip()[4:-4]).difference('a', 'c', 'i', 't', 'n'))

# k가 5 미만이라면 어떤 단어도 만들 수 없다.
if k < 5:
    print(0)
else:
    bin_list = [word_to_bin(x) for x in words]
    max_count = 0

    # 2의 0제곱부터 2의 20제곱까지 저장
    power_of_2 = []
    for i in range(21):
        power_of_2.append(2 ** i)

    for comb in combinations(power_of_2, k - 5):
        current = sum(comb)
        count = 0
        for bin_number in bin_list:
            # 바깥쪽 for문 - 현재 순회 중인 k - 5개의 알파벳 조합(comb)으로
            # 안쪽 for문 - 현재 순회 중인 단어를 만들 수 있다면
            if bin_number & current == bin_number:
                count += 1
        max_count = max(max_count, count)
    print(max_count)
