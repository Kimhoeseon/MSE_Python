import random   #무작위 숫자를 뽑기 위해 random 사용


class Account:
    account_count = 0  #class variable: 변수 생성

    def __init__(self, name, balance): # __init__ 로 인스턴스 생성
        self.deposit_count = 0         # 예금횟수 초기값을 0으로 설정
        self.deposit_log = []
        self.withdraw_log = []         # 예금,출금 내역 리스트로 구성

        self.name = name
        self.balance = balance
        self.bank = "SC은행"           # name의 자리에 이름, balance의 자리에 잔고 저장

       
       # randint()함수로 구간 내에 숫자를 무작위로 가져온다.
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        # 무작위로 뽑은 수를 문자열 str로 변경, 자릿수를 맞추기 위해 zfill() 메서드 사용
        num1 = str(num1).zfill(3)  
        num2 = str(num2).zfill(2)  
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3   # 계좌번호 생성
        Account.account_count += 1                             # 계좌번호 개수

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  

    def deposit(self, amount):                 #객체에 접근하기 위해 self 사용, 입금액을 amount로 바인딩
        if amount >= 1:                        # 1원 이상일 때 입금 가능
            self.deposit_log.append(amount)
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:        # 예금 내역이 증가했을 때 5의 배수를 확인     
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount):
        if self.balance > amount:           #잔고가 출금 요청액보다 많은지 확인
            self.withdraw_log.append(amount)
            self.balance -= amount

    def display_info(self):               # Account 인스턴스에 저장된 정보를 출력하는 display_info 메서드 
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):           # 출금 금액을 출금 내역에서 가져와 출력
        for amount in self.withdraw_log:
            print(amount)
  
    def deposit_history(self):            # 입금 금액을 입금 내역에서 가져와 출력
        for amount in self.deposit_log:
            print(amount)

# 클래스 Account 안의 변수들에 접근, 객체 적용 
k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()