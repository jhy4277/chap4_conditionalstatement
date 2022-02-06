# 논리연산자(logical operator)는 두 개 이상의 조건을 조합해서 참인지 거짓인지를 계산할 때 사용하는 연산자이다.
# 논리연산자의 종류에는 and, or, not이 있다.
# and 논리 연산자의 실습
name="정혜원"
age=14
height=160


if(age>=15)and (height>=160) and (name=="정혜원"):
    print("놀이 기구를 탈 수 있습니다.")
else:
    print("놀이기구를 탈 수 없습니다.")