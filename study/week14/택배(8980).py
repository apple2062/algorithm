# 택배 ( https://www.acmicpc.net/problem/8980 )
n, c = map(int,input().split()) # 마을 수, 트럭의 최대 용량
m = int(input()) # 보내는 박스 정보의 개수
lst = []
max_box = [c]*(n)
for i in range(m):
    from_,to_,box = map(int,input().split())
    lst.append((from_,to_,box))
# 받는 마을이 빠른 순서로 정렬시킴 (to_ 순으로 정렬)
lst.sort(key = lambda x: x[1])
answer = 0

for i in range(len(lst)):
    min_ = c+ 1
    print(lst[i])
    # 배송을 받기 전 마을들의 수용가능한 개수
    for j in range(lst[i][0], lst[i][1]):
        if max_box[j]< min_ :
            min_ = max_box[j]
    # 현재 마을에서 실을 수 있는 박스의 개수 중 작은 값
    val = min(min_,lst[i][2])
    answer += val
    print("min , val, answer : ", (min_,val,answer))
    # 각 마을을 돌며 val 만큼 수용가능한 박스 개수를 빼준다.
    for j in range(lst[i][0], lst[i][1]):
        max_box[j] -= val
    print("max_box : " ,max_box)
print(answer)



