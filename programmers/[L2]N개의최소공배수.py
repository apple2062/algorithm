# N개의 최소공배수 (https://programmers.co.kr/learn/courses/30/lessons/12953)
# make LCM using gcd library !!!
# >> LCM -> (a*b) // gcd(a,b)

def solution(arr):
    from math import gcd
    def lcm(a,b):
        return a*b // gcd(a,b)
    
    while len(arr)>1:
        arr.append(lcm(arr.pop(),arr.pop()))
    
    return arr[0]
