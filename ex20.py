# 중복 nested if ~ else 구문
# 사용자로부터 아이디를 입력받아서 등록되어진 아이디인지 검사하는 프로그램을 작성하는데, 등록된 아이디를 list에 저장하도록 한다.
# 아이디가 등록되어있다면 패스워드를 물어보도록 한다. 패스워드는 "1234"라고 가정한다.
# 아이디들의 값들을 리스트에 저장하는 코드

user_list=["정혜원", "박성현","빌게이츠","김연아","지창욱"]
pw="1234"
id=input("아이디를 입력하세요:")

if id in user_list: # 사용자가 입력한 id 가 user_list에 있는지 확인하는 코드
    password=input("패스워드를 입력하세요: ")
    if password==pw:
        print(id + "님이 로그인 하셨습니다.")
    else:
        print("패스워드가 틀렸습니다.")
else:
    print("회원가입이 되지 않았습니다.")