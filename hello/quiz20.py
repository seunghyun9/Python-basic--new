import random
import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


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

    def quiz24zip(self) -> {}:
        url ='https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')#html.parser vs lxml(이름임)
        #print(soup.prettify())
        #print(Quiz20.found(soup, 'artist'))
            # print(''.join(i for i in [i for i in self.found(soup, j)]))
        # a = [i for i in self.found(soup, 'artist')]
        # a = [i for i in self.found
        # (soup, 'title')]
        cls_names = ['artist', 'title']
        a = [i for i in cls_names]
        ls1 = self.found(soup, 'title')
        ls2 = self.found(soup, 'artist')
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
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
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            #print(type(f'타입: {ls1[i]}'))
            dict[ls1[i]] = ls2[i] #키값과 벨류값을 출력함 키값:밸류값 << 출력
        print(dict)

    def print_music_list(self, soup) -> None:
        artists = soup.find_all('p', {'class': 'artist'})
        artists = [i.get_text() for i in artists]
        print(''.join(i  for i in artists))
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_rank(self,soup):
          for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(self.found(soup,j)):
                 print(f'{i}위 :{j}')
            print('*' * 100)

    @staticmethod
    def found(soup, cls_nm) -> []:
        find = soup.find_all('p', {'class': cls_nm})
        return [i.get_text() for i in find]
        # print(type(artists))


    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> {}:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(),'lxml')
        cls_name2=['checkEllipsis','ellipsis rank01']
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


        '''
        a= [i if i==0 or i==0 else i for i in range()] #수열
        b= [i if i ==0 or i==0 else i for i in[]]
        c= [(i,j) for i ,j in enumerate([])]
        d= = ''.join(i for i in[])
        '''


    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index') #내부적으로 엑셀시트형식으로 만듬
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN') #sep = 구분값 , na_rep=비어있으면공백을둬라

        return None

    def quiz29(self) -> str: return None

