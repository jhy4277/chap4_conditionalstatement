# 사용자로부터 태어난 연도를 입력받아서 초등학생, 중학생, 고등학생, 혹은 대학생 분류중 어디에 해당하는지 출력하는 프로그램
# 나이 : 8~13(초등학생), 14~16(중학생), 17~19(고등학생), 20~27(대학생) 이 외의 나이라면 일반인으로 분류

age= int(input("나이를 입력하세요: "))

if (age>=8) and (age<=13):
    print("초등학생")
elif (age>=14) and (age<=16):
    print("중학생")
elif (age>=17) and (age<=19):
    print("고등학생")
elif (age>=20) and (age<=27):
    print("대학생")
else:
    print("일반인")