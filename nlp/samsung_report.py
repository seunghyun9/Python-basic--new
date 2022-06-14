from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import nltk
import re
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from icecream import ic
import tweepy
from context.domains import Reader, Printer, File
import nltk
'''
    문장 형태의 문자 데이터를 전처리할 때 많이 사용되는 방법이다. 
    말뭉치(코퍼스 corpus)를 어떤 토큰의 단위로 분할하냐에 따라 
    단어 집합의 크기, 단어 집합이 표현하는 토크의 형태가 다르게 나타나며 
    이는 모델의 성능을 좌지우지하기도 한다. 
    이때 텍스트를 토큰의 단위로 분할하는 작업을 토큰화라고 한다. 
    토큰의 단위는 보통 의미를 가지는 최소 의미 단위로 선정되며, 
    토큰의 단위를 단어로 잡으면 Word Tokenization이라고 하고, 
    문장으로 잡으면 Sentence Tokeniazation이라고 한다. 
    영어는 주로 띄어쓰기 기준으로 나누고, 
    한글은 단어 안의 형태소를 최소 의미 단위로 인식해 적용한다.
    형태소(形態素, 영어: morpheme)는 언어학에서 의미가 있는 가장 작은 말의 단위이다.
    1. Preprocessing : kr-Report_2018.txt 를 읽는다.
    2. Tokenization
    3. Token Embedding
    4. Document Embedding
    
    형태소(形態素, 영어: morpheme)는 언어학에서 의미가 있는 가장 작은 말의 단위이다.
코퍼스(영어: corpus) 말뭉치는 언어학에서 주로 구조를 이루고 있는 텍스트 집합이다.
코퍼스(corpus)는 단어들을 포함한다.
임베딩(embedding)은 변환한 벡터들이 위치한 공간이다.
단어(word)는 일반적으로 띄어쓰기나 줄바꿈과 같은 공백 문자(whitespace)로 나뉘어져 있는 문자열의 일부분이다.
단어를 벡터로 변환하는 경우 단어 임베딩(word embedding)이다. 
각 문장을 벡터로 변환하는 경우 문장 임베딩(sentence embedding)이다. 
단어 임베딩이란 앞서 말씀드린 바와 같이 이 각각 하나의 좌표를 가지도록 형성한 벡터공간이다.

'''

class Solution(Reader):
    def __init__(self):
        self.okt = Okt()
        self.file = File()
        self.file.context = './data/'

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. Preprocessing')
            print('2. Tokenization')
            print('3. Token Embedding')
            print('4. Document Embedding')
            print('5. 2018년 삼성사업계획서를 분석해서 워드클라우드를 작성하시오.')
            print('9. nltk download')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                self.preprocessing()
            elif menu == '2':
                self.tokenization()
            elif menu == '3':
                self.token_embedding()
            elif menu == '4':
                self.document_embedding()
            elif menu == '5':
                self.draw_worldcloud()
            elif menu == '9':
                Solution.download()

    @staticmethod  # 클래스와 상관 없이 미리 존재함
    def download():
        nltk.download('punkt')

    def preprocessing(self):
        self.okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        file = self.file
        file.fname = 'kr-Report_2018.txt'
        path = self.new_file(file)
        with open(path, 'r', encoding='utf-8') as f:
            texts = f.read()
        texts = texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ㄱ-힣]+')
        return tokenizer.sub(' ', texts)

    def tokenization(self):
        noun_tokens = []
        tokens = word_tokenize(self.preprocessing())
        # ic(tokens[:100])
        for i in tokens:
            pos = self.okt.pos(i)
            _ = [j[0] for j in pos if j[1] == 'Noun']
            if len(''.join(_)) > 1:
                noun_tokens.append(' '.join(_))
        texts = ' '.join(noun_tokens)
        ic(texts[:100])
        return texts

    def read_stopword(self):
        self.okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        file = self.file
        file.fname = 'stopwords.txt'
        path = self.new_file(file)
        with open(path, 'r', encoding='utf-8') as f:
            texts = f.read()
        ic(texts)
        return texts
    def remove_stopword(self):
        tokens = self.tokenization()
        stopword = self.read_stopword()
        texts = []
        print(texts)

    def token_embedding(self):
        pass

    def document_embedding(self):
        pass

    def draw_worldcloud(self):
        pass


if __name__ == '__main__':
    print(tweepy.__version__)
    Solution().hook()
