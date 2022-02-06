# 몸무게와 키를 입력받고 BMI가 20.0이상이고 25 미만이면 표준입니다라고 출력하고 아니면 체중관리가 필요합니다.
# BMI= 몸무게/ 키의제곱
# 키를 100.0으로 나눈다.

height=float(input("키를 입력 : "))
weight=float(input("몸무게를 입력 :"))

height/=100.0
bmi= weight / (height ** 2)
print("bmi: ",bmi)

if (bmi>=20.0) and (bmi<25.0):
    print("표준입니다.")
else:
    print("체중관리가 필요합니다.")