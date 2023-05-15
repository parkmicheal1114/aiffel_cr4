from datetime import datetime # 주문표에 주문 일시 같이 출력하기 위해 datetime 모듈 불러오기

# 전체 메뉴와 가격 2차원 리스트로 표현
menu_price = [['americano', 'latte', 'mocha', 'yuza_tea', 'green_tea', 'choco_latte'], 
              [2000, 3000, 3000, 2500, 2500, 3000]]

class Kiosk: 
    def __init__(self):
        self.menu = menu_price[0]
        self.price = menu_price[1]

    # 메뉴 출력 메서드
    def menu_print(self):
        for i in enumerate(zip(self.menu, self.price)):
            num, menu_and_price= i
            menu, price = menu_and_price
            print(num+1, menu, ':', price, '원')

    # 주문 메서드
    def menu_select(self):
        self.order_menu = []  # 주문 리스트
        self.order_price = []  # 가격 리스트

        n = 0
        # 첫 번째 음료 선택
        while n < 1 or len(self.menu) < n:
            n = int(input("음료의 번호를 입력하세요 : "))  # 음료 번호 입력

            # 메뉴판에 있는 음료 번호일 때
            if 1 <= n & n <= len(self.menu):
                self.order_price.append(self.price[n-1])  # 가격 리스트에 추가합니다.
                self.price_sum = self.price[n-1]  # 합계 금액
            
                # 메뉴판에 없는 번호일 때
            else:  
                print("없는 메뉴입니다. 다시 주문해 주세요.")


        # 음료 온도 물어보기
        t = 0  # 기본값을 넣어주고
        while t != 1 and t != 2:  # 1이나 2를 입력할 때까지 물어보기
            t= int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))
            temp = ''
            self.temp = temp          
            if t == 1:
                self.temp = "HOT"
            elif t == 2:
                self.temp = 'ICE'  
            else:    
                print("1과 2 중 하나를 입력하세요.\n")

        self.order_menu.append(self.temp + ' ' + self.menu[n-1])  # 주문 리스트에 추가합니다.
        print(self.temp, self.menu[n-1], ' : ', self.price[n-1], '원')  # 온도 속성을 추가한 주문 결과를 출력합니다.

        # 추가 주문 또는 지불
        while n != 0:  # 지불을 선택하기 전까지 반복합니다.
            print()  # 줄 바꾸면서 
            n = int(input("추가 주문은 음료 번호를, 지불은 0을 누르세요 : "))  # 추가 주문 또는 지불
            if n > 0 and n < len(self.menu) + 1: 
                # 추가 음료 온도 
                t = 0
                while t != 1 and t != 2:
                    t = int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))
                    if t == 1:
                        self.temp = "HOT"
                    elif t == 2:
                        self.temp = "ICE"
                    else:
                        print("1과 2 중 하나를 입력하세요.\n")
                self.order_menu.append(self.temp + ' ' + self.menu[n-1])
                self.order_price.append(self.price[n-1])
                self.price_sum += self.price[n-1]
                print('추가 주문 음료', self.temp, self.menu[n-1], ':', self.price[n-1], '원\n', '합계 : ', self.price_sum, '원')
            else :
                if n == 0 :  # 지불을 입력하면
                    print("주문이 완료되었습니다.")
                    print("주문하신 메뉴는 ")
                    for i in zip(self.order_menu, self.order_price):
                        print(i)
                    print("입니다.")  # 주문 확인 리스트 출력
                else :  # 없는 번호를 입력할 때
                    print("없는 메뉴입니다. 다시 주문해 주세요.")
        
    # 결제 메서드
    def pay(self):
        pay_with = ''
        print(f'지불하실 금액은 {self.price_sum}입니다.')
        check = 1
        while check == 1:           # 결제가 제대로 이루어졌는지 체크하기 위해 check가 1인동안 결제 계속 체크, 오류 발생했을 시 다시 시도하도록 구성
            pay_with = input('지불 수단을 입력해주세요. 예시:\n\t현금 결제:cash or 1 \n\t카드 결제:card or 2 \n\t')
            if pay_with == 'cash' or pay_with == '1':
                print('직원을 호출하겠습니다.')
                check = 0
            elif pay_with == 'card' or pay_with == '2':
                print('IC칩 방향에 맞게 카드를 꽂아주세요.')
                check = 0
            else:
                print('다시 결제를 시도해 주세요.')
    
    # 주문표를 감싸는 데코레이터 만들기
    def deco(fn):
        def wrapper(self):
            print('⟝' + '-' * 30 + '⟞')
            for i in range(5):
                print('|' + ' ' * 31 + '|')
            fn(self)
            for i in range(5):
                print('|' + ' ' * 31+ '|')
            print('⟝' + '-' * 30 + '⟞')  
        return wrapper  
    
    # 주문표 출력하기
    @deco
    def table(self):
        # 현재 날짜-시각을 불러와 주문표에 출력하기
        print('\t' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        print('\t주문 목록')
        for i, j in zip(self.order_menu, self.order_price):
            print('\t' + i, ' : ', j)
            
        print()
        print('\t합계 금액 :', self.price_sum)   
        

a = Kiosk()  # 객체 생성 
a.menu_print()  # 메뉴 출력
print()
a.menu_select()  # 주문
print()
a.pay()  # 지불
print()
a.table()  # 주문표 출력