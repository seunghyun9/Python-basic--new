import random
import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np
from quiz00 import Quiz00
from hello import Member
from hello.domains import my100, myRandom, members


class Quiz20:

    def quiz20list(self):
        list1 = [1, 2, 3, 4]
        print(list1, type(list1))
        print(list1[0], list1[-1], list1[-2], list1[1:3])

        list2 = ['math', 'english']
        list2[0]
        list2[0][1]

        list3 = [1, '2', [1, 2, 3]]
        list3

        list4 = [1, 2, 3]
        list5 = [4, 5]
        list4 + list5
        2 * list4
        list4.append(list5)
        list4
        list4[-2:] = 1
        list4

        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        c
        c[0][1]
        c[0][1] = 10
        c

        a1 = range(10)
        a1
        sum(a)
        b2 = [2, 10, 0, -2]
        sorted(b)
        b2.index(0)
        len(b)
        print(b2.index(0), len(b))

    def quiz21tuple(self):
        a = (1, 2)
        print(a, type(a))
        a[0] = 4  # 에러메시지 출력
        a = (1, 2)
        b = (0, (1, 4))
        a + b

    def quiz22dict(self):
        a = {"class": ['deep learning', 'machine learning'], "num_student": [40, 20]}
        type(a)
        a["class"]
        a['grade'] = ['A', 'B''C']
        a
        a.key()
        list(a.keys())
        a.values()
        a.items()
        a.get('class')
        "class" in a

    def quiz23listcom(self) -> str:
        print('-----------legacy-----------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('-----------comprehension-----------')
        a2 = [i for i in range(5)]
        print(a2)
        return None

    def quiz24zip(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')  # html.parser vs lxml(이름임)
        # print(soup.prettify())
        # print(Quiz20.found(soup, 'artist'))
        # print(''.join(i for i in [i for i in self.found(soup, j)]))
        # a = [i for i in self.found(soup, 'artist')]
        # a = [i for i in self.found
        # (soup, 'title')]
        ls1 = self.found(soup, 'title')
        ls2 = self.found(soup, 'artist')

        a = [i if i == 0 or i == 0 else i for i in range(1)]  # 수열
        b = [i if i == 0 or i == 0 else i for i in []]
        c = [(i, j) for i, j in enumerate([])]
        d = {i: j for i, j in zip(ls1, ls2)}
        l = [i + j for i, j in zip(ls1, ls2)]
        l2 = list(zip(ls1, ls2))
        d1 = dict(zip(ls1, ls2))
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        print(dict)
        return dict

        '''
        artists = soup.find_all('p', {'class':'artist'})
        artists = [i.get_text() for i in find]
        # print(type(artists))
        print(''.join(i  for i in artists))
        
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))
        '''
        ''' 
         for i in range(3):
            print(artists[i].text.strip())
        '''

    @staticmethod
    def dict3(ls1, ls2) -> None:
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            # print(type(f'타입: {ls1[i]}'))
            dict[ls1[i]] = ls2[i]  # 키값과 벨류값을 출력함 키값:밸류값 << 출력
        print(dict)

    def print_music_list(self, soup) -> None:
        artists = soup.find_all('p', {'class': 'artist'})
        artists = [i.get_text() for i in artists]
        print(''.join(i for i in artists))
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_rank(self, soup):
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(self.found(soup, j)):
                print(f'{i}위 :{j}')
            print('*' * 100)

    @staticmethod
    def found(soup, cls_nm) -> []:
        find = soup.find_all('p', {'class': cls_nm})
        return [i.get_text() for i in find]
        # print(type(artists))

    def quiz25dictcom(self) -> str:
        # members()[myRandom(0, 23)] 이것이 1명인데 5명 추출 ,quiz06을 import로 호출
        # scores는 0~100점 사이에서 랜덤
        q = Quiz00
        student = set([q.quiz06memberChoice() for i in range(5)])
        while len(student) != 5:
            student.add(q.quiz06memberChoice())
        c = list(student)
        scores = [myRandom(0, 101) for i in range(5)]
        '''
        dict = {}
        for i, j in zip(student, scores):
            dict[i] = j
        print(dict)
        return None
          '''
        print({i: j for i, j in zip(c, scores)})

    # if i == i or i == 6 else str(myRandom(1, 10)) for i in range(5))

    def quiz26map(self) -> str:
        return None

    def quiz27melon(self) -> {}:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        cls_name2 = ['checkEllipsis', 'ellipsis rank01']
        a2 = [i for i in cls_name2]
        '''
        artists = soup.find_all('span', {'class': 'checkEllipsis'})
        titles = soup.find_all('div', {'class':'ellipsis rank01'})
        titles = [i.get_text() for i in titles]
        artists = [i.get_text() for i in artists]
         #print(type(artists))
        print(''.join(i for i in titles))
        print(''.join(i for i in artists))
        '''
        ls3 = self.found2(soup, 'checkEllipsis')
        ls4 = self.found3(soup, 'ellipsis rank01')
        dict2 = {}
        for i, j in zip(ls3, ls4):
            dict2[i] = j
        print(dict2)
        return dict2

    @staticmethod
    def found2(soup, cls_nm) -> []:
        find = soup.find_all('span', {'class': cls_nm})
        return [i.get_text() for i in find]

    @staticmethod
    def found3(soup, cls_nm) -> []:
        find = soup.find_all('div', {'class': cls_nm})
        return [i.get_text() for i in find]

    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index')  # 내부적으로 엑셀시트형식으로 만듬
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')  # sep = 구분값 , na_rep=비어있으면공백을둬라

        return None

    def quiz29_pandas(self) -> object:  # 데이터 프레임은 오브젝트로 바꿔야함
        '''
        다음결과 출력
            a   b   c
        1   1   2   3
        2   2   4   6
        '''
        d = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
        df1 = pd.DataFrame(d, index=[1, 2])
        d2 = {"1": [1, 3, 5], "2": [2, 4, 6]}
        df2 = pd.DataFrame.from_dict(d2, orient='index', columns=['a', 'b', 'c'])
        columns1 = [chr(i) for i in range(97, 100)] # ['a','b','c']

        e1 = []
        e2 = []
        [e1.append(i) if i % 2 != 0 else e2.append(i) for i in range(1, 7)]
        d3 = {"1": e1, "2": e2}
        df3 = pd.DataFrame.from_dict(d3, orient='index', columns=columns1)

        print(df3)
        return None
