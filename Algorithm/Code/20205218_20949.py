import math
arr = []
N=int(input())
for i in range(N):
    Wi, Hi = map(int,input().split())# 2 4
    PP = math.sqrt(Wi**2+Hi**2) / 77
    arr.append((PP,i+1))
#내림차순과 오름차순을 적용
arr.sort(key = lambda x: (-x[0], x[1]))

for j in arr:
    print(j[1])