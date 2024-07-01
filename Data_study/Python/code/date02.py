# 날짜/시간과 관련된 기능 가지고오기
import datetime

# 현재 날짜/시간을 구함
now = datetime.datetime.now()

# 오전 구분
if now.hour < 12:
  print("현재 시각은 {}시로 오전입니다".format(now.hour))

# 오후 구분
if now.hour >= 12:
  print("현재 시각은 {}시로 오후입니다".format(now.hour))
