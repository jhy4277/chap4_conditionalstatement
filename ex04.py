# 불(bool)변수 알아보기
# 부울변수의 용도는 플래그 변수 형태로 사용을 많이 한다.
flag= True
print(type(flag))
print(flag)

flag=not flag
print(type(flag))
print(flag)

if flag:
    print("참이라서 실행됩니다.")
else:
    print("거짓이라서 실행됩니다.")
    flag= not flag