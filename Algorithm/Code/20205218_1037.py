N = int(input()) #N의 약수의 개수
b =[]
a = input().split()# 2 4
for i in a:
    b.append(int(i))
print(min(b)*max(b))
