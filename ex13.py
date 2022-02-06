#대학교를 졸업하려면 적어도 140 학점을 이수해야 하고, 평점은 2.0은 되어야 한다고 해보자

hak=float(input("이수한 학점을 입력해주세요:"))
grade=float(input("평점을 입력하세요: "))

if(hak>=140) and (grade>=2.0):
    print("졸업가능")
else:
    print("졸업불가능")