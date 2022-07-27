n = int(input())
arr = []
# 입력 받는 부분
for _ in range(n):
    li = list(map(int, input().split()))
    arr.append(li)

tmp = []
result = []

# 마지막 2x2가 나올 때 까지 반복문 실행
while len(arr) != 2:
    result = []
    len_of_row = len(arr) # 현재 row의 길이를 알려줌,

    for row in range(0, len_of_row-1, 2): # Stride = 2, 2칸씩 뛰어 넘어감
        for col in range(0, len_of_row-1, 2): # Stride = 2, 2칸씩 뛰어 넘어감,
            # -1을 해주는 이유는 마지막 Filter가 돌 때 Index out of range Error를 뛰어넘기 위해

            filter = [] # 2x2 크기의 필터 순회
            for f_row in range(row, row+2):
                for f_col in range(col, col+2):
                    filter.append(arr[f_row][f_col])

            # 필터를 돌아서 나온 값 저장 후 2번째로 큰 값만 추출해서 저장
            tmp.append(sorted(filter)[-2])

            # nxn 크기가 (n//2)x(n//2) 가 될 수 있게 조절해주는 부분
            if len(tmp)%(len_of_row//2) == 0:
                result.append(tmp)
                tmp = []

    arr = result

pred = []
for element in arr:
    for e in element:
        pred.append(e)
print(sorted(pred)[-2])