N = int(input())
Ai = int(input())
B,C = input().split()
B=int(B)
C=int(C)
total = 0
if(Ai-B > 0):
    total = total +1
    if((Ai-B)%C == 0):
        total = total + 1
    else:
        total = total + (Ai-B)//C + 1
else:
    total = 1
print(N * total)

