# 정수
output_a = "{: d}".format(52)

# 특정 칸에 출력
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

# 빈칸 0 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# 기본")
print(output_a)
print("# 특정 칸에 출력")
print(output_b)
print(output_c)
print("# 빈칸 0 채우기")
print(output_d)
print(output_e)
