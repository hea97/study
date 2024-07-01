# 날짜/시간과 관련 기능 가져오기
import datetime

# 현재 날짜/시간 구하기
# 쉽게 사용할 수 있게 우러을 변수에 저장
now = datetime.datetime.now()
month = now.month

# 조건문 계절을 확인
if 3 <= month <= 5:
  print("현재 봄")
elif 6 <= month <= 8:
  print("현재 여름")
elif 9 <= month <= 11:
  print("현재 가울")
else:
  print("현재 겨울")
