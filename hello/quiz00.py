import random

from hello import Member
from hello.domains import my100, myRandom, members


class Quiz00:
    def quiz00calculator(self) -> float:
        a = my100()
        b = my100()
        o = ["+", "-", "*", "/", "%"]  # 백터값
        if (o[myRandom(0, 4)] == '+'):  # 스칼라값을 뽑아내야함
            res = self.add(a, b)
        if (o[myRandom(0, 4)] == '-'):
            res = self.sub(a, b)
        if (o[myRandom(0, 4)] == '*'):
            res = self.mul(a, b)
        if (o[myRandom(0, 4)] == '/'):
            res = self.div(a, b)
        if (o[myRandom(0, 4)] == '%'):
            res = self.mod(a, b)
        print(res)

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(self):
        this = Member()
        this.name = members()[myRandom(0, 23)]
        this.height = myRandom(130, 200)
        this.weight = myRandom(130, 200)
        bmi2 = this.weight / (this.height * this.height) * 10000
        if bmi2 > 25:
            res = f'키:{this.height} 몸무게:{this.weight} 비만'
        elif bmi2 > 23:
            res = f'키:{this.height} 몸무게:{this.weight} 과체중'
        elif bmi2 > 18.5:
            res = f'키:{this.height} 몸무게:{this.weight} 정상'
        else:
            res = f'키:{this.height} 몸무게:{this.weight} 저체중'
        print(res)

    def quiz02dice(self):
        print(myRandom(1, 6))

    def quiz03rps(self):
        c = myRandom(1, 3)
        p = myRandom(1, 3)
        # 1 가위 2  바위 3 보
        rps = ['가위', '바위', '보']
        print(' ----------- 1 ------------')
        if p == 1:
            if c == 1:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[0]}, 결과: 무승부'
            elif c == 2:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[1]}, 결과: 패배'
            elif c == '3':
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[2]}, 결과: 승리'
        elif p == 2:
            if c == 1:
                res = '승리'
            elif c == 2:
                res = '무승부'
            elif c == 3:
                res = '패배'
        elif p == 3:
            if c == 1:
                res = '패배'
            elif c == 2:
                res = '승리'
            elif c == 3:
                res = '무승부'
        else:
            res = '1~3 입력'
        print(res)
        print(' ----------- 2 ------------')
        if p == c:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:무승부'
        elif p - c == 1 or p - c == -2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:승리'
        elif p - c == -1 or p - c == 2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:패배'
        else:
            res = '1~3 입력'
        print(res)

    def quiz04leap(self):
        year = myRandom(0, 2021)
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            res = f'{year}년은 윤년'
        else:
            res = f'{year}년은 평년'
        print(res)

    def quiz05grade(self):
        name = members()[myRandom(0, 23)]
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = self.sum(kor, eng, math)
        avg = self.avg(kor, eng, math)
        grade = self.grade(kor, eng, math)
        passChk = self.passChk(kor, eng, math)

        print(f'{name}님, 국어 점수 : {kor} \n ' \
              f'영어 점수 : {eng}\n 수학 점수: {math}\n' \
              f'총합: {sum} 평균: {avg} 등급: {grade} 합격 여부: {passChk}')
        return None

    def sum(self, kor, eng, math):
        return kor + eng + math

    def avg(self, kor, eng, math):
        return self.sum(kor, eng, math) / 3

    def passChk(self, kor, eng, math):  # 60점 이상 이면 합격
        return '합격' if self.avg(kor, eng, math) >= 60 else '불합격'

    def grade(self, kor, eng, math):
        if (self.avg(kor, eng, math)) >= 90:
            return 'A등급'
        elif (self.avg(kor, eng, math)) >= 70:
            return 'B등급'
        elif (self.avg(kor, eng, math)) >= 50:
            return 'C등급'
        elif (self.avg(kor, eng, math)) >= 30:
            return 'D등급'
        else:
            return 'F등급'

    def quiz06memberChoice(self):
        return members()[myRandom(0, 23)]

    def quiz07lotto(self):
        lotto1 = set([])  # set([])을 이용하여 중복값 제거
        while len(lotto1) < 6:
            lotto1.add(myRandom(1, 45))
        print(lotto1)

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        print(' ----------- 1 ------------')
        name = members()[myRandom(0, 23)]
        add = myRandom(0, 5000000)
        out = myRandom(0, 5000000)
        res = f'이름:{name} \n입금금액:{add}, 출금금액:{out} 잔고:{add - out}'
        print(res)

        print(' ----------- 2 ------------')
        Account.main()

    def quiz09gugudan(self):  # 책받침 구구단
        for a in range(1, 10):
            for b in range(2, 10):
                print(b, 'x', a, '=', b * a, end='\t')  # end='\t'를 이용하여 단위곱셈간 간격구분
            print()  # 한 싸이클 마다 줄바꿈


'''
은행이름은 Bitbank
입금자 이름(name), 계좌번호(acoount_number), 금액(money) 속성값으로 계좌를 생성한다.
계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성된다.ex 123-12-123456
금액은 100~999사이로 랜덤하게 입금된다(단위는 만단위로 암묵적으로 판단)
'''


class Account(object):
    def __init__(self, name, account_number, money):
        num1 = myRandom(0, 999)
        num2 = myRandom(0, 99)
        num3 = myRandom(0, 999999)
        '''
        num1 = str(num1).zfill(3) # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2) # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6) # 1 -> '1' -> '0000001'
        '''
        self.account_number = f'{num1:0>3}-{num2:0>2}-{num3:0>6}'
        self.BANK_NAME = '비트은행'
        self.name = Quiz00().quiz06memberChoice() if name is None else name
        self.money = myRandom(100, 1000) if money is None else money
        self.create_account_number = self.create_account_number() if account_number is None else account_number

    def to_string(self):
        return f'은행: {self.BANK_NAME},\n' \
               f'임금자:{self.name}\n' \
               f'계좌번호:{self.create_account_number}\n' \
               f'금액:{self.money} 만원'

    def create_account_number(self):
        '''
        ls=[str(myRandom(0,10)) for i in range(3)]
        ls=ls.append("-")
        ls= [str(myRandom(0, 10)) for i in range(2)]
        ls=ls.append("-")
        ls= [str(myRandom(0, 10)) for i in range(6)]
        return "".join(ls) # " "=문자열(객체) join=문자열결합
        '''
        return ''.join([str(myRandom(0, 9)) if (i != 3 and i != 6) else '-' for i in range(13)])

    def del_account(self, ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.계좌개설 2.계좌목록 3.입금 4.출금 5.계좌해지')
            if menu == '0':
                break
            if menu == '1':
                acc = Account(None,None,None)
                print(f'{acc.to_string()}... 개설되었습니다.')
                ls.append(acc)
            elif menu == '2':
                a = '\n'.join(w.to_string() for w in ls)
                print(a)
            elif menu == '3':
                account_number = input('입금할 계좌번호')
                money = input('입금액')
                for i, j in enumerate(ls):
                    if j.account_number == account_number:
                        pass

                # 추가코드 완성
            elif menu == '4':
                account_number = input('출금할 계좌번호')
                money = input('출금액')
            elif menu == '5':
                account_number = input('탈퇴할 계좌번호')
            else:
                print("Wrong number .. Try Again")
                continue
