# 숫자 고르기 ( https://www.acmicpc.net/problem/2668)
'''
문제 유형 dfs 인거 보고 너무 황당했음.... 첫시도에 combinations 썼다가 당연하게 TLE 떴음

dict에 대한 while 문 돌려주었다
'''

n = int(input())
dic = {}
for i in range(n):
    dic[i + 1] = int(input())

while True:
    dic_set = set(dic.values())
    dic = {key: value for key, value in dic.items() if key in dic_set}
    print(dic_set, dic.values())
    if dic_set == set(dic.values()):
        break

print(len(dic))
for i in dic.keys():
    print(i)
