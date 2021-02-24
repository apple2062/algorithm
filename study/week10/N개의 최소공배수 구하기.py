# N개의 최소 공배수 구하기 for using "gcd" library
'''
 2개의 수에 대해 최소공배수를 구한 후, 그 값과 계산하지 않은 값들 중 1개를 선택하여 다시 최소공배수를 구한다.

'''
from math import gcd

def solution(arr):

    def lcm(x,y):
        return x*y // gcd(x,y)

    while True:
        arr.append(lcm(arr.pop(),arr.pop()))
        if len(arr) == 1:
            return arr[0]

print(solution([2,6,8,14]))
