a = 3
b = 5

print ( a ==3 and b == 5 ) # True 출력
print ( a ==3 and b != 5 ) # False 출력
print ( a ==3 or b != 5 ) #  True 출력


"""
사과는 냉장실에
아이스크림은 냉동실에 넣어 주시고,
나머지는 폐기처분 해주세요.

"""

변수 = "사과"

if 변수 == "사과":
  print("냉장실")
elif 변수 == "아이스크림":
  print("냉동실")
else :
  print("폐기처분")