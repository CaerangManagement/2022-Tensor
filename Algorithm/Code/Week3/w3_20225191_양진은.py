
#문제1
#백준 제출 성공
N = int(input()) #시험장 개수
Ai = [int(i) for i in input().split()] #응시자 수
B, C = (int(i) for i in input().split()) # B 총감독관, C 부감독관

res = 0
for person in Ai:
  person_B = person - B
  if person_B <= 0:
    res +=1
  else:
    if person_B - C <= 0:
      res += 2
    else:
      res += 1 #총감독
      if person_B % C > 0:
        res += (person_B // C + 1) #부감독
      else:
        res += person_B // C

print(res)

#문제2

#백준 시간 초과, 힙 정렬 구현하다 던짐

#입력처리
X = 0
Y = 1
def inputLine(line: int) -> list:
  Line = []
  for _ in range(line):
    x, y = input().split()
    x = int(x)
    y = int(y)
    Line += [[x, y]]
  return Line

def print_coordinate(coordinate: list) -> None:
  for i in coordinate:
    print(i[X],i[Y])

#버블정렬
def sorted_coordinate_bo(coordinate: list) -> None:
  def swith(i):
    tmp = coordinate[i+1]
    coordinate[i+1] = coordinate[i]
    coordinate[i] = tmp
    return
  for j in range(len(coordinate)):
    for i in range(0, len(coordinate) - j - 1):
      if coordinate[i][X] > coordinate[i+1][X]:
        swith(i)
      if coordinate[i][X] == coordinate[i+1][X] and coordinate[i][Y] > coordinate[i+1][Y]:
        swith(i)
  return

#선택 정렬
def sorte_sorted_coordinate_sel(coordinate: list) -> None:
  res_lis = []
  def getMin(ls):
    min = ls[0]
    for i in ls:
      if i[X] < min[X]:
        min = i
      if i[X] == min[X] and i[Y] < min[Y]:
        min = i
    return min
  for _ in range(len(coordinate)):
    m = getMin(coordinate)
    coordinate.remove(m)
    res_lis += [m]
  return res_lis

#힙 정렬
#좌표간 크기 비교 a > b 
def size_comparison(a:list, b:list):
  X = 0
  Y = 1
  if a[X] > b[X]:
    return True
  elif a[X] == b[X] and a[Y] > b[Y]:
    return True
  else:
    return False

#노드 정렬
def heapfly(li:list, idx:int, n:int):
  l_node = idx*2
  r_node = idx*2 + 1
  s_idx = idx #비교대상
  if l_node <= n and size_comparison(li[s_idx], li[l_node]):
    s_idx = l_node
  if r_node <= n and size_comparison(li[s_idx], li[r_node]):
    s_idx = r_node
  if s_idx != idx:
    li[idx], li[s_idx] = li[s_idx], li[idx]
    return heapfly(li, s_idx, n)
  

#
def sorte_sorted_coordinate_heap(coordinate):
  coordinate = [0] + coordinate
  n= len(coordinate)

  for i in range(n-1, 0, -1):
    heapfly(coordinate, 1, i)

  for i in range(n-1, 0, -1):
    print(coordinate[1][X], coordinate[1][Y])
    coordinate[i], coordinate[1] = coordinate[1], coordinate[i]
    heapfly(coordinate, 1, i-1)

      
# sorted_coordinate_bo(coordinate)
# print_coordinate(coordinate)
#coordinate = inputLine(int(input()))
c = inputLine(int(input()))
sorte_sorted_coordinate_heap(c)

#문제3

#백준 제출 성공

# 코드 개형
# 1 <= n <= 1000000 소수 리스트 Pi 생성
# a - 입력받은 수 - Pi 가 소수라면 두 수의 차를 구하고 추가
# Pi > 입력수 일때까지 a과정을 반복, 두 수의 차가 더 클 경우 업데이트 -> 어차피 앞에 걸로 해도 되지 않을까?
# 위 과정을 반복

#에리토테네스의 체
def makePrime():
  n = 1000000
  a = [False, False] + [True]*(n-1) #자연수 제외
  prime = []
  for i in range(2, n+1):
    if a[i]:
      prime += [i]
      for j in range(2*i, n+1, i):
        a[j] = False
  return prime

def inputLine3()-> list:
  ls = []
  while True:
    u = int(input())
    if u == 0:
      break
    ls += [u]
  return ls

Prime_list = makePrime()
Prime_set = set(Prime_list) #set이 속도가 빠름
ls = inputLine3()

for num in ls:
  j = 0
  a = 0
  b = 0
  #c = 0
  while num > Prime_list[j]:
    _b = num - Prime_list[j]
    if _b in Prime_set:
      a = Prime_list[j]
      b = _b
      break
    j+=1
  if a == 0:
    print("Goldbach's conjecture is wrong")
  else:
    print(f"{num} = {a} + {b}")