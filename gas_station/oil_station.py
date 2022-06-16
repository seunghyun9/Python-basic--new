from selenium import webdriver
import time
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc  # 한글 시각화 패키지 설치

from context.domains import Reader


# https://velog.io/@changhtun1/Python-%EB%8F%99%EC%A0%81-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81


class Solution(Reader):
    def __init__(self):
        pass

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. 크롤링(엑셀파일 다운로드)')
            print('2. 임베딩')
            print('3. 정형화')
            print('4. 데이터 시각화')
            print('5. 데이터 통계화')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                self.crawling()
            elif menu == '2':
                self.embedding()
            elif menu == '3':
                self.stereotype()
            elif menu == '4':
                self.visualization()
            elif menu == '5':
                self.statistics()

    def crawling(self):
        driver = webdriver.Chrome('C:/Users/seunghyun/PycharmProjects/djangoProject/gas_station/data/chromedriver.exe')
        driver.get("http://www.opinet.co.kr/searRgSelect.do")
        driver.get("https://www.opinet.co.kr/searRgSelect.do")
        # 구 선택 id 정보 얻기
        driver.find_element_by_id("SIDO_NM0").send_keys('서울특별시')  # 1st 리스트 박스를 찾아서 강원도 선택
        second_list_raw = driver.find_element_by_id("SIGUNGU_NM0")
        time.sleep(1)  # 첫번째 리스트를 선택하고 대기 필수
        second_list = second_list_raw.find_elements_by_tag_name("option")  # 2nd 리스트 박스에서 옵션리스트 뽑기

        # 리스트 만들기
        option_values = []
        for option in second_list:
            option_values.append(option.get_attribute("value"))
        option_values.remove('')  # 빈 문자 제거

        # 반복문으로 모든 구 데이터 다운로드하기
        for cnt in range(len(option_values)):
            second_list_raw = driver.find_element_by_id("SIGUNGU_NM0")  # 키 입력을 서울특별시로 선택
            second_list_raw.send_keys(option_values[cnt])  # 키 입력을 구 번호 차례대로 선택
            time.sleep(3)
            file_down = driver.find_element_by_id('glopopd_excel').click()  # 엑셀 저장버튼 누르기, 저장확인

        driver.close()  # 브라우저 (드라이브)종료

    def embedding(self):
        # 여러 개의 엑셀파일을 하나의 리스트에 담기
        print(glob('data/지역*.xls'))  # '지역'으로 시작되는 모든 xls 파일명을 리스트에 담기
        merged_list = glob('data/지역*.xls')  # 새로운 리스트에 저장
        list_tabel = []  # 엑셀 내용을 담을 리스트
        for file_name in merged_list:
            tmp = pd.read_excel(file_name, header=2)
            list_tabel.append(tmp)
        total_gas_station = pd.concat(list_tabel)  # 25개의 테이블을 하나의 리스트 구조로 반환
        return total_gas_station

    def stereotype(self):  # 정형화
        # 분석에 필요한 테이블 재구성
        total_gas_station = self.embedding()
        gas_station = pd.DataFrame({'주유소명':
                                        total_gas_station['상호'], \
                                    '경유가격': total_gas_station['경유'], \
                                    '셀프': total_gas_station['셀프여부'], \
                                    '브랜드': total_gas_station['상표'], \
                                    '주소': total_gas_station['주소']})
        gas_station = gas_station[gas_station['경유가격'] != '-']  # 경유 가격이 없는 데이터 삭제
        gas_station['경유가격'] = [float(value) for value in gas_station['경유가격']]  # 가격 정보를 실수형으로 변환
        gas_station.reset_index(inplace=True)  # 1열 인덱스 번호 재지정
        return gas_station

    def visualization(self): # 데이터 시각화
        self.korean_font()
        gas_station = self.stereotype()
        gas_station.boxplot(column='경유가격', by='셀프')  # 셀프 VS 비셀프 가격 비교
        plt.show()
        sns.boxplot(x='브랜드', y='경유가격', hue='셀프', data=gas_station)  # 브랜드별 가격 분포
        plt.show()
        sns.boxplot(x='셀프', y='경유가격', hue='브랜드', data=gas_station)  # 브랜드별 셀프 VS 비 셀프 가격 비교
        plt.show()

    def statistics(self): # 데이터 통계화
        gas_station = self.stereotype()
        print(gas_station.sort_values(by='경유가격', ascending=False).head(10))
        print(gas_station.sort_values(by='경유가격', ascending=True).head(10))

    @staticmethod
    def korean_font():  # 한글깨짐 방지, 폰트설정
        path = "c:/Windows/Fonts/malgun.ttf"
        font_name = font_manager.FontProperties(fname=path).get_name()
        rc('font', family=font_name)


if __name__ == '__main__':
    Solution().hook()
