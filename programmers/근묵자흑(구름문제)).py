#구름 (근묵자흑)
#https://level.goorm.io/exam/47881/%EA%B7%BC%EB%AC%B5%EC%9E%90%ED%9D%91/quiz/1
n,k = map(int,input().split())
matrix = list(map(int,input().split()))
tmp = n-k
res = 1
if tmp%(k-1) == 0:
    res += (tmp//(k-1))
else:
    res += (tmp//(k-1) + 1)
print(res)
