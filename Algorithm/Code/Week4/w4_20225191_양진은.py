#문제1 

#백준 제출 성공
#길게 작성 했는데 결국 최소값, 최대값의 곱

#최소공배수 구하기
def getLeastCommonMultiple(min: int, max:int):
  if min > max: return 0
  min_prime_factors: list = primeFactorization(min)
  commonFactor = []

  for pf in min_prime_factors:
    if (0 == min % pf) and (0 == max % pf):
      commonFactor += [pf]
      min = min // pf
      max = max // pf
    else:
      break
  
  commonFactor += [min, max]
  res = 1
  for i in commonFactor:
    res *= i
  return res

#소인수 분해
def primeFactorization(num):
  prime_factor = list()
  d = 2
  while d <= num:
    if 0 == num % d:
      num = num // d
      prime_factor += [d]
    else:
      d +=1
  return prime_factor

def getMax(nums):
  max_idx = 0
  for idx in range(1, len(nums)):
    if nums[max_idx] < nums[idx]:
      max_idx = idx
  return nums[max_idx]

def getMin(nums):
  min_idx = 0
  for idx in range(1, len(nums)):
    if nums[min_idx] > nums[idx]:
      min_idx = idx
  return nums[min_idx]

input()
factor = [int(i) for i in input().split()]
max_factor = getMax(factor)
min_factor = getMin(factor)

lcm = getLeastCommonMultiple(min_factor, max_factor)
if lcm == max_factor:
  lcm *= min_factor

print(lcm)

#줄인 버전, 백준 제출 완료
def getMax(nums):
  max_idx = 0
  for idx in range(1, len(nums)):
    if nums[max_idx] < nums[idx]:
      max_idx = idx
  return nums[max_idx]

def getMin(nums):
  min_idx = 0
  for idx in range(1, len(nums)):
    if nums[min_idx] > nums[idx]:
      min_idx = idx
  return nums[min_idx]

input()
factor = [int(i) for i in input().split()]
max_factor = getMax(factor)
min_factor = getMin(factor)

print(max_factor*min_factor)

######################################################
#문제2
#백준 제출 성공
import math

def inputLine(line_count:int):
  PPI_res = []
  for i in range(line_count):
    W, H = input().split()
    PPI_res += [[PPI(int(W), int(H)), i]]
  return PPI_res

def PPI(W:int, H:int, D=77):
  return math.sqrt((W**2) + (H**2)) / D

def findSort(ls):
  for i in range(len(ls)):
    max_ppi = i
    for j in range(i+1, len(ls)):
      if ls[j][0] > ls[max_ppi][0]:
        max_ppi = j
      elif ls[j][0] == ls[max_ppi][0]:
        if ls[j][1] < ls[max_ppi][1]:
          max_ppi = j
    ls[max_ppi], ls[i] = ls[i], ls[max_ppi]
  return ls

res = findSort(inputLine(int(input())))
for i in res:
  print(i[1]+1)


######################################################
#문제3
#pypy3 제출 성공
#python3 시간초과

def inputLine(K):
  res = []
  for i in range(K):
    res += [[int(i) for i in input().split()]]
  return res

#색을 섞는다.
def mixRGB(colors: list, K):
  R = sum([color[0] for color in colors]) // K
  G = sum([color[1] for color in colors]) // K
  B = sum([color[2] for color in colors]) // K
  return [R, G, B]

#색의 차이를 비교
def colorCompare(RGB1:list, RGB2:list):
  #_abs = (lambda x : x*(-1) if x < 0 else x)
  return abs(RGB1[0] - RGB2[0]) + abs(RGB1[1] - RGB2[1]) + abs(RGB1[2] - RGB2[2])

def mixcColorCompare(mixColors, gomColor):
  compareLs = []
  for mixColor in mixColors:
    compareLs += [colorCompare(mixColor, gomColor)]
  return compareLs

def mixmix(colors: list) -> list:
  colorsSize = len(colors)
  mixls = []
  for a in range(colorsSize):

    if (2 > colorsSize) : continue
    for b in range(a+1, colorsSize):
      mixls += [mixRGB([colors[a], colors[b]], 2)]

      if (3 > colorsSize) : continue
      for c in range(b+1, colorsSize):
        mixls += [mixRGB([colors[a], colors[b], colors[c]], 3)]

        if (4 > colorsSize) : continue
        for d in range(c+1, colorsSize):
          mixls += [mixRGB([colors[a], colors[b], colors[c], colors[d]], 4)]

          if (5 > colorsSize) : continue
          for e in range(d+1, colorsSize):
            mixls += [mixRGB([colors[a], colors[b], colors[c], colors[d], colors[e]], 5)]

            if (6 > colorsSize) : continue
            for f in range(e+1, colorsSize):
              mixls += [mixRGB([colors[a], colors[b], colors[c], colors[d], colors[e], colors[f]], 6)]

              if (7 > colorsSize) : continue
              for g in range(f+1, colorsSize):
                mixls += [mixRGB([colors[a], colors[b], colors[c], colors[d], colors[e], colors[f], colors[g]], 7)]
  return mixls
                
K = int(input())
colors = inputLine(K) #물감
gom = [int(i) for i in input().split()] #곰두리색

#믹스믹스
mix = mixmix(colors)
mixGom = mixcColorCompare(mix, gom)

#내장함수 사용
print(min(mixGom))
