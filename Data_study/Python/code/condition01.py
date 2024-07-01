# 입력 받기
number = input("정수 입력> ")

# 마지막 자리 숫자 출력
last_character = number[-1]

# 숫자로 변환
last_number = int(last_character)

# 짝수 확인
if last_number == 0 \
  or last_number == 2 \
  or last_number == 4 \
  or last_number == 6 \
  or last_number == 8:
    print("짝수")

# 홀수 확인
if last_number == 1 \
  or last_number == 3 \
  or last_number == 5 \
  or last_number == 7 \
  or last_number == 9:
    print("홀수")
    
