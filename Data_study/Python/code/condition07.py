# 변수 선언
score = float(input("학점 입력> "))

# 조건문 적용
if score == 4.5:
  print("신")
elif 4.2 <= score:
  print("교수님의 사랑")
elif 3.5 <= score:
  print("현 체제의 수호자")
elif 2.8 <= score:
  print("일반인")
elif 2.3 <= score:
  print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score:
  print("오락문화의 선구자")
elif 1.0 <= score:
  print("불가촉천민")
elif 0.5 <= score:
  print("자벌레")
elif 0 <score:
  print("플랑크톤")
else:
  print("시대를 앞서가는 혁명의 씨앗")
