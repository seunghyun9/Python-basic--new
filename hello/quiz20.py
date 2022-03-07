import random


class Quiz20:

    def quiz20list(self):
        list1=[1,2,3,4]
        print(list1,type(list1))
        print(list1[0],list1[-1],list1[-2],list1[1:3])

        list2=['math','english']
        list2[0]
        list2[0][1]

        list3=[1,'2',[1,2,3]]
        list3

        list4=[1,2,3]
        list5=[4,5]
        list4+list5
        2*list4
        list4.append(list5)
        list4
        list4[-2:]=1
        list4

        a=[1,2]
        b=[0,5]
        c=[a,b]
        c
        c[0][1]
        c[0][1]=10
        c

        a1=range(10)
        a1
        sum(a)
        b2=[2,10,0,-2]
        sorted(b)
        b2.index(0)
        len(b)
        print(b2.index(0),len(b))

    def quiz21tuple(self):
        a=(1,2)
        print(a,type(a))
        a[0]=4 #에러메시지 출력
        a=(1,2)
        b=(0,(1,4))
        a+b

    def quiz22dict(self):
        a={"class": ['deep learning','machine learning'],"num_student":[40,20]}
        type(a)
        a["class"]
        a['grade']=['A','B''C']
        a
        a.key()
        list(a.keys())
        a.values()
        a.items()
        a.get('class')
        "class"in a


    def quiz23listcom(self) -> str:
        print('-----------legacy-----------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('-----------comprehension-----------')
        a2 = [ i for i in range(5)]
        print(a2)
        return None

    def quiz24zip(self) -> str: return None

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27(self) -> str: return None

    def quiz28(self) -> str: return None

    def quiz29(self) -> str: return None