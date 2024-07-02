list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거")

# 제거 방법[1] - del 키워드
del list_a[1]
print("del list_a[1]:", list_a)

# 제거 방법[2] - pop()
list_a.pop(2)
print("pop(2) : ", list_a)
