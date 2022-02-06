# 숫자 추측게임

from random import *
rand_num=randint(1,100)
print("발생한 난수 :",rand_num)
cnt=1
user_num=int(input("숫자를 맞춰보세요: "))
while True:
    if user_num==rand_num:
        print("정답","시도횟수:",cnt)
        break
    elif user_num>rand_num:
        print("입력한 숫자가 큽니다.")
        cnt+=1
    else:
        print("숫자가 작습니다.")
        cnt+=1

    user_num=int(input("다시 입력해주세요 : "))
