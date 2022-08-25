#백준 제출
def inputLine(lc : int):
  return [input() for i in range(lc)]

def score_cal_sh(quiz_answer):
  return sum([sum(range(1, len(i)+1)) for i in quiz_answer.split("X")])

t = [print(score_cal_sh(i)) for i in inputLine(int(input()))]

def score_cal(quiz_answer):
  score = 0
  continuity = 0
  for answer in quiz_answer:
    if "O" == answer:
      score += continuity + 1
      continuity += 1
    elif "X" == answer:
      continuity = 0
  return score

#재미로 해본 숏코딩! 제출 성공!
[print(sum([sum(range(1, len(i)+1)) for i in i.split("X")])) for i in [input() for i in range(int(input()))]]
[print(sum([sum(range(1, len(i)+1)) for i in input().split("X")])) for i in range(int(input()))] #백준에서는 정답인데 약간 다르게 작동

#문제2
b = [0, 1]
for _ in range(int(input())):
  b += [sum(b[-2:])]
print(b[-2])

#문제 3 백준 제출 완료
#처음부터 이렇게 작성하는 바람에...
input() 
print(sum([1 if i != 1 and sum([1 if 0 == i % j else 0 for j in range(2, i)]) == 0 else 0 for i in [int(k) for k in input().split()]]))

#문제4
#각각의 순서쌍을 구한뒤 집합 연산, 메모리 초과
#각각의 이어진 경우를 구하고, 교집합을 구하는 방식
#->알고리즘을 잘못 작성한 것 같음, 슬라이싱으로 인해 메모리 초과가 발생하는 줄 알았으나, C++로 동일 코드 작성해도, 메모리 초과 발생.(객체배열, 구조체보다 크기가 크다.)

def makeSet(ls, size):
  res = []
  n = 1
  while size >= n:
    #슬라이싱이 메모리를 많이 먹는 듯 함
    res += [(ls[n], i) for i in ls[n:]]
    n+=1
  return res

def compareSet(lsA, ls, size):
  res = 0
  n = 1
  while size >= n:
    for i in ls[n:]:
      if (ls[n], i) in lsA:
        res += 1
    n+=1
  return res

s = int(input())
q = input().split()
a = input().split()
qset = set(makeSet(q, s))
res = compareSet(qset, a, s)

print(f"{res}/{len(qset)}")

# print(f"{len(qset & aset)}/{len(aset)}")

#set(makeSet(list(range(5))))

#문제 5
#최대 괄호의 개수를 구한다.
#괄호를 이동하며 구한다.
#괄호의 크기 고려
#나누는 방법

#생각한 대로 하면 원하는 결과가 안나올 것 같음
#반복문 구상이 안되서 포기....

#idea
#브루트 포싱?

import re

exp = input()
exp_ls = []
back = ""
for i in exp:
  if i == "+" or i == "-":
    exp_ls += [int(back)]
    exp_ls += [i]
    back = ""
  else:
    back += i

exp_ls += [int(back)]

op_count = len(exp_ls) // 2 #연산자의 개수
num_count = len(exp_ls) - op_count #숫자의 개수 #최대 괄호의 수

for i in range(2, num_count + 1): #괄호안의 숫자 갯수
  for j in range(num_count // i):
    pass
    