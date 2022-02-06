# if ~ elif ~ else(옵션) 대한 실습
score= int(input("성적을 입력하세요 :"))
# 다중 조건 중 하나만 만족하면 그 이후의 조건은 검사하지 않는다.(중요)
if score >=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")