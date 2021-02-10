# 팀 결성 (10-02)

# 학생 0-n 번까지 처음 총 n+1 개의 팀
# 팀 합치기 (연산 형태 : 0) , 같은 팀 여부 확인(연산 형태 : 1) 연산 가능
# 선생님이 m 개의 연산을 수행할 수 있을 떄, '같은팀여부확인' 연산에 대한 연산 결과 출력하는 프로그램

def union(p,a,b):
    a  = rootnode(p,a)
    b = rootnode(p,b)
    if a<b:
        p[b] = a
    else:
        p[a] = b
    
def rootnode(p,node):
    if p[node] != node:
        p[node] = rootnode(p,p[node])
    return p[node]

n,m = map(int,input().split()) # 학생 끝 번호, 연산의 개수
p = [0] * (n)
for i in range(p):
    p[i] = i

for _ in range(m):
    oper,a,b = map(int,input().split())
    if oper == 0: # 팀 합치기 연산이라면
        union(p,a,b)
    elif oper == 1: # 같은 팀 여부 확인 연산이라면
        if rootnode(p,a) != rootnode(p,b):
            print("NO")
        else:
            print("YES")

