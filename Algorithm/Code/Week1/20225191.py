# 과제1
def di(n, m, loop, zero=False):
  #print(f"[loop{loop}]")
  if(loop == 1): print(".", end="")
  if (loop == 21): return
  #뒤를 0으로 채운다
  elif zero:
    print("0", end="")
    di(0, 0, loop+1, True)
  #나머지가 0이 아닐시 나머지에 10을 곱하고 재귀
  elif n % m != 0:
    print(str(n // m), end="")
    di((n%m)*10, m, loop+1)
  #나눗셈 종료, 뒤를 0으로 채운다.
  elif n % m == 0:
    print(n // m, end="")
    di(0, 0, loop+1, True)
  #현재 몫으로 나누기가 불가능한 경우
  elif n // m == 0:
    print("0", end="")
    di(n*10, m, loop+1)

a, b = input("").split()
a = int(a)
b = int(b)

di(a, b, 0)

#과제2
def P(n:int, k:int = 1):
  if k > n:
    #반복이 하나 증가한 상태이므로
    return k - 1
  return P(n-k, k+1)

"""
서로 다른 N개의 자연수를 더한 값을 구할 시
결론적으로 1부터 차례로 더하며, 채워나가야한다.
마지막 과정에서 그 이상 더하면 S를 초과할 경우
마지막 자연수 + 남은 자연수의 크기를 더한다면, 자연수 S가 만들어진다.(서로 다른 N개의 자연수)
"""

num = int(input(""))
P(num)

#과제3
import numpy as np
import math

#입력처리부
def arrInput():
  size = int(input(""))
  resArr = []
  for i in range(size):
    tem = input("").split()
    tem = [int(i) for i in tem]
    resArr += [tem]
  return resArr

def getSecondMax(twoDimArr:list) -> int:
  #2*2 리스트에서만 유효
  sortArr = []
  for oneDim in twoDimArr:
    for j in oneDim:
      sortArr += [j]
  sortArr.sort(reverse=True)
  return sortArr[1]

    
def pooling222(twoDimArr:list) -> int:
  count = len(twoDimArr)
  #print(count)
  tem = np.array(twoDimArr)
  twoTwoList = []

  #2*2 배열로 쪼갠다
  for i in range(0, count, 2):
    for j in range(0, count, 2):
      twoTwoList += [(tem[i:i+2, j:j+2]).tolist()]
  secondMaxLs = []
  #2*2 배열을 순회하며 2번째로 큰 값을 구한다.
  for i in twoTwoList:
    secondMaxLs += [getSecondMax(i)]
  #print(len(secondMaxLs))

  if len(secondMaxLs) == 1:
    return secondMaxLs[0]
  
  #2차원으로 변경필요
  npArr = np.array(secondMaxLs)
  s = int(math.sqrt(npArr.size))
  npArr = npArr.reshape(s, s)
  return pooling222(npArr.tolist())
    
ls = arrInput()
a = pooling222(ls)
print("res=",a)