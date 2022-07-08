# 문제 1
import decimal # 소수점을 정확하게 계산하기 위해 고정 소수점 사용
context = decimal.getcontext()
context.rounding = decimal.ROUND_FLOOR # decimal의 자리 올림 방식을 내림으로 변경

a, b = input().split() # 입력값을 공백을 기준으로 분리하여 입력받기
a = decimal.Decimal(a) # 입력받은 값을 decimal로 형변환
b = decimal.Decimal(b)

result = a / b
print(f"{result:.20f}")


# 문제 2
def find_max(val) : # 자연수 N의 최댓값을 찾는 함수 
    sum = 0 # 1부터 자연수의 합 S까지 더한 결과를 저장할 변수
    max = 0 # 자연수 N의 최댓값을 저장할 변수 
    for i in range(1, val) : 
        sum += i
        if (sum > val) :
            max = i 
            break
    max = max - 1
    print(max)

num = int(input()) # 서로 다른 N개의 자연수의 합 S 입력받기
find_max(num)