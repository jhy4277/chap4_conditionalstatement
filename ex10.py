# 쇼핑몰에서 물건을 구매할 때, 구입액이 5만원 이상이면 5%의 할인을 해준다고 하자.
# 사용자에게 구입 금액을 입력받고 최종적으로 할인 금액과 지불금액을 출력하는 프로그램 만들기

total_price=int(input("구입금액을 입력하세요 : "))

if total_price>=50000:
    discount=total_price*0.05
    sales_price=total_price-discount
    print("구입금액 : ",total_price)
    print("할인금액: ",discount)
    print("지불액: ",sales_price)

else:
    print("할인금액 대상이 되지 않습니다.", total_price,"원을 지불해주세요")