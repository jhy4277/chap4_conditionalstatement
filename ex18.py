# 주사위 눈을 랜덤으로 발생시켜서 해당하는 숫자를 출력하는 프로그램을 만들기
# randint() 함수를 검색하여 사용법을 익힌 후 프로그램을 작성하시오.

from random import *
#randint(a,b)함수는 a부터 b까지의 사이에 있는 정수를 반환해주는 함수
#num=randint(1,6)
#print("주사위 눈: ", num)

# random() 함수는 0.0부터 1.0미만의 임의의 값을 float 형태로 반환해주는 함수
#num=random()
#print("num : ",num)

# randrange(start, stop,step) 함수는 start에서 stop까지 step의 값에 따라서 임의의 수를 반환을 해주는 함수
#num=randrange(1,101,2)
#print("num : ",num)

# randrange(a) 함수는 0부터 a미만의 임의의 정수값을 반환하는 함수
#num=randrange(10)
#print("num : ",num)

num=randint(1,6)
print("주사위눈 : ",num)

if num==1:
    print("주사위 눈: ", 1)
elif num==2:
    print("주사위 눈:", 2)
elif num==3:
    print("주사위 눈:", 3)
elif num==4:
    print("주사위 눈:", 4)
elif num==5:
    print("주사위 눈:", 5)
else:
    print("주사위 눈 : ",6)