# 6-4 두 배열의 원소 교체
# 시간복잡도 O(N log N)


# 두 배열의 원소 하나 k번 바꿔서 A 배열의 합이 최대각 되도록

n,k = map(int,input().split())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())),reverse=True)
for i in range(k):
    if a[i]<b[i]:
        a[i],b[i] = b[i],a[i]
print(sum(a))
