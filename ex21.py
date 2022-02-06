# 학점을 세부적으로 나누는 프로그램을 작성하기(중첩 if)
# 1. 사용자로부터 점수를 입력받는다.
# 2. 점수가 95 점 100 이하라면 A+
# 3. 점수가 90 이상 94 이하라면 A
# 4. B,C,D도 위와같이 출력한다.
# 5. 단, F는 그냥 출력하도록 하자.

score=int(input("점수를 입력하세요 : "))
grad= ""
print("입력한 점수: ", score)

if score >=90:
    if score>=95:
        grade= "A+"
    else:
        grade= "A"
elif score >=80:
    if score>=85:
        grade= "B+"
    else:
        grade= "B"
elif score >=70:
    if score>=75:
        grade= "C+"
    else:
        grade= "C"
elif score >=60:
    if score>=65:
        grade= "D+"
    else:
        grade= "D"
else:
    print("점수: ", score, "학점 : F")

print("점수: ", score, "학점 : ", grade)