# 숫자 입력
raw_input = input("inch 단위 숫자를 입력 : ")

# 입력받은 데이터를 숫자 자료형으로 변경, cm단위로 변경
inch = int(raw_input)
cm = inch * 2.54

# 출력
pirnt(inch, "inch는 cm단위로", cm, "cm 입니다.")
