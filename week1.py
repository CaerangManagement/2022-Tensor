#문제1
from decimal import Decimal
import math

a, b = input().split()

a = Decimal(a)
b = Decimal(b)
re = a/b

print("{:.20f}".format(re))

#문제2
S=int(input())
i=1
cnt=0
while 1: 
    cnt = cnt+1
    S = S-i
    if (S<=i) or (S==0):
       break;
    i = i+1
print(cnt)