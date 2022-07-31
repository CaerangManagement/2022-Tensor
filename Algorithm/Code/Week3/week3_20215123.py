#문제1
N = int(input())   #시험장 개수
Ai = list(map(int, input().split()))   #각 시험장에 있는 응시자 수
B,C = map(int, input().split())   #총감독관,  부감독관이 감시 가능한 응시자 수
cnt=0   #필요한 감독관 수

for i in Ai:
    student = i-B
    cnt+=1
    if student > 0 :
        cnt += (i-B)//C
        if (i-B)%C != 0:
            cnt += 1
print(cnt)

#문제3
arr = []
for i in range(3,1000001,2): #10000000까지의 소수 구하기
    cnt=0 #1과 자기자신 외 나누어 떨어지는 수의 개수
    for j in range (3, i):
        if(i%j==0): #(1과 자기자신 외에) 나누어 떨어지는 수가 있으면
            cnt += 1
    if(cnt == 0):
        arr.append(i) #없으면 배열에 추가
print(arr)

arrTest = []
while True: #입력받기
    n = int(input())
    if(n==0):
        break
    arrTest.append(n)

for j in arrTest:
    for i in arr:
       if (j-i) in arr:
          print(j,"=",i,"+",(j-i))
          break
