
n = int(input())
a =[]
for i in range(n):
    n1,n2=map(int,input().split())
    a.append((n1,n2))
a.sort()


for i in range(n):
    print(a[i][0],a[i][1])

