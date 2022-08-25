# 8958

t = int(input())

for i in range(t):
    OX = list(input())
    
    sum = 0
    cnt = 1
    
    for i in OX:
        if i == 'O':
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)
    

# 2748

n = int(input())
fib = [i for i in range(n+1)]
fib[1] = 1

for i in range(2, n+1) :
    fib[i] = fib[i-1] + fib[i-2]
    
print(fib[-1])


# 1978

num = int(input())
n = map(int, input().split())
ss = 0

for i in n:
    ev = 0
    if i > 1:
        for j in range(2, i):
            if  i % j == 0:
                ev += 1

        if ev == 0:
            ss += 1
print(ss)


# 3077

n = int(input())
dab = input().split()
dict_ = {}

for i in range(n):
    dict_[dab[i]] = i

h_dab = input().split()
cnt = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if dict_[h_dab[i]] < dict_[h_dab[j]]:
            cnt += 1
print(f"{cnt}/{n * (n - 1) // 2}")
