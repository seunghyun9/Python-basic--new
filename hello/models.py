import random
class Quiz01Calculator:

    def __init__(self, num1,opcode, num2):
        self.num1 = num1
        self.opcode=opcode
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def mul(self):
        return self.num1 * self.num2

    def min(self):
        return self.num1 - self.num2

    def div(self):
        return self.num1 / self.num2

    def calc(self):
        if self.opcode == 1:
            res = self.num1 + self.num2
        if self.opcode == 2:
            res= self.num1 - self.num2
        if self.opcode == 3:
            res= self.num1 * self.num2
        if self.opcode ==4:
            res= self.num1 / self.num2
        return print(f'{self.num1} {self.opcode} {self.num2} = {res}')


class Quiz02Bmi:
    @staticmethod #이닛이 아닌 게터세터를 쓰겠다는 의미
    def getbmi(member):
       this = member
       total = this.weight /(this.height * this.height) * 10000
       if total >= 35:
           print(f'BMI:{total:.2f} 고도 비만')
       if total > 25 and total <= 34.9:
           print(f'BMI:{total:.2f} 비만')
       if total > 18.5 and total <= 24.9:
           print(f'BMI:{total:.2f} 정상')
       if total < 18.5:
           print(f'BMI:{total:.2f} 저체중')

class Quiz03Grade:
    def __init__(self, kor, eng, math,):
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return self.kor + self.eng + self.math
    def res(self):
        avg = (self.total()) / 3
        if avg>= 60:
            print(f'총점:{self.total()} 평균:{avg:.2f} 합격')
        else:
            print(f'총점:{self.total()} 평균:{avg:.2f} 불합격')

class Quiz04GradeAuto:
    def __init__(self, kor, eng, math,):
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return self.kor + self.eng + self.math
    def getGrade(self):
        pass
    def chkPass(self):
        pass

def myRandom(start,end):
    return random.randint(start,end)

class Quiz05Dice:
    @staticmethod
    def ran():
        return myRandom(1,6)

class Quiz06RabdomGenerator(object):
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def pick(self):
        return print(f'{random.randint(self.num1, self.num2)}')

class Quiz07RandomChoice(object):
    def __init__(self): # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜' , '권솔이', '김지혜' , '하진희' , '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]
    def chooseMember(self):
        return self.members[myRandom(0,23)]
    '''def choice(self):
        choiceMember = random.choice(self.members)
        return print(f'{choiceMember}')'''

class Quiz08Rps(object):
    def __init__(self,user):
        self.user = user
        self.com = myRandom(1,3)

    def game(self):
        p= self.user
        c= self.com
        # 1 가위 2 바위 3보자기
        rps = ['가위', '바위', '보']
        if p==c:
            res= f'플레이어:{rps[p-1]}, 컴퓨터:{rps[c-1]}, 결과:무승부'
        elif p-c == 1 or p-c == -2:
            res= f'플레이어:{rps[p-1]}, 컴퓨터:{rps[c-1]}, 결과:승리'
        elif p - c == -1 or p-c == 2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:패배'
        else:
            res = '올바른 숫자를 입력 해주세요.'
        return res


        '''if p == 1:
            if c==1:
                res= f'플레이어:{rps[0]},컴퓨터:{rps[0]}, 결과:무승부'
            elif c==2:
                res= f'플레이어:{rps[0]},컴퓨터:{rps[1]}, 결과:패배'
            elif c==3:
                res= f'플레이어:{rps[0]},컴퓨터:{rps[2]}, 결과:승리'
        elif p==2:
            if c == 1:
                res = f'플레이어:{rps[1]},컴퓨터:{rps[0]}, 결과:승리'
            elif c == 2:
                res = f'플레이어:{rps[1]},컴퓨터:{rps[1]}, 결과:무승부'
            elif c == 3:
                res = f'플레이어:{rps[1]},컴퓨터:{rps[2]}, 결과:패배'
        elif p==3:
            if c==1:
                res= f'플레이어:{rps[2]},컴퓨터:{rps[0]}, 결과:패배'
            elif c==2:
                res= f'플레이어:{rps[2]},컴퓨터:{rps[1]}, 결과:승리'
            elif c==3:
                res= f'플레이어:{rps[2]},컴퓨터:{rps[2]}, 결과:무승부'
        else:
            res= '올바른 숫자를 입력 해주세요.'
        return res'''



class Quiz09GetPrime(object):
    def __init__(self):
        pass
class Quiz10LeapYear(object):
    def __init__(self):
        pass
class Quiz11NumberGolf(object):
    def __init__(self):
        pass
class Quiz12Lotto(object):
    def __init__(self):
        pass
class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self):
        pass
class Quiz14Gugudan(object): # 책받침구구단
    def __init__(self):
        pass