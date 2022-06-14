from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import pyautogui
import pandas as pd
from glob import glob

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc # 한글 시각화 패키지 설치
path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=path).get_name()
rc('font', family=font_name)
#https://velog.io/@changhtun1/Python-%EB%8F%99%EC%A0%81-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81



class Oil_Station:
    def __init__(self):
        pass

    def seoul_station_price(self):
        driver = webdriver.Chrome('C:/Users/seunghyun/Downloads/chromedriver_win32/chromedriver.exe')
        driver.get("http://www.opinet.co.kr/searRgSelect.do")
        driver.get("https://www.opinet.co.kr/searRgSelect.do")
        xpath = """//*[@id="SIDO_NM0"]"""
        gu_list_raw = driver.find_element_by_xpath("SIGUNGU_NM0")
        gu_list = gu_list_raw.find_elements_by_tag_name("option")
        gu_names = [option.get_attribute("value") for option in gu_list]
        gu_names.remove('')
        print(gu_names)

    def test(self):
        driver = webdriver.Chrome('C:/Users/seunghyun/Downloads/chromedriver_win32/chromedriver.exe')
        driver.get("http://www.opinet.co.kr/searRgSelect.do")
        driver.get("https://www.opinet.co.kr/searRgSelect.do")
        time.sleep(3)
        # driver.close()
        print(pyautogui.position())
        time.sleep(1)
        driver.find_element_by_id("SIDO_NM0").send_keys('서울특별시')  # 1st 리스트 박스를 찾아서 강원도 선택
        second_list_raw = driver.find_element_by_id("SIGUNGU_NM0")
        time.sleep(1)  # 첫번째 리스트를 선택하고 대기 필수
        second_list = second_list_raw.find_elements_by_tag_name("option")
        # 2nd 리스트 박스에서 옵션리스트 뽑기
        option_values = []
        for option in second_list:
            option_values.append(option.get_attribute("value"))
        option_values.remove('')  # 빈 문자 제거
        print(option_values)

        second_list_raw.send_keys('강북구')  # 키 입력을 강북구로 선택
        # second_list_raw.send_keys(option_values[2]) # 키 입력을 강북구로 선택
        time.sleep(3)
        # 엑셀 저장버튼 누르기, 저장확인
        file_down = driver.find_element_by_id('glopopd_excel').click()
        time.sleep(3)
        # 강서구 다운로드 받아 보기
        second_list_raw = driver.find_element_by_id("SIGUNGU_NM0")
        second_list_raw.send_keys('강서구')  # 또는 option_values[3]
        time.sleep(3)
        file_down = driver.find_element_by_id('glopopd_excel').click()
        time.sleep(3)
        for cnt in range(len(option_values)):
            second_list_raw = driver.find_element_by_id("SIGUNGU_NM0")
            second_list_raw.send_keys(option_values[cnt])  # 키 입력을 차례대로 선택
            time.sleep(3)
            file_down = driver.find_element_by_id('glopopd_excel').click()

    @staticmethod
    def test2():
        print(glob('./data2/지역*.xls'))  # '지역'으로 시작되는 모든 xls 파일명을 리스트에 담기
        merged_list = glob('./data2/지역*.xls')  # 새로운 리스트에 저장

        list_tabel = []  # 엑셀 내용을 담을 리스트
        for file_name in merged_list:
            tmp = pd.read_excel(file_name, header=2)
            list_tabel.append(tmp)

        print(list_tabel)  # 25개의 테이블이 저장된 리스트
        total_gas_station = pd.concat(list_tabel)  # 25개의 테이블을 하나의 리스트구조로 반환
        print(total_gas_station)

        gas_station = pd.DataFrame({'주유소명':
                                        total_gas_station['상호'], \
                                    '경유가격': total_gas_station['경유'], \
                                    '셀프': total_gas_station['셀프여부'], \
                                    '브랜드': total_gas_station['상표'], \
                                    '주소': total_gas_station['주소']})
        print(gas_station)

        print(gas_station.info())
        gas_station = gas_station[gas_station['경유가격'] != '-']
        print(gas_station.info())

        gas_station['경유가격'] = [float(value) for value in gas_station['경유가격']]
        print(gas_station.info())

        gas_station.reset_index(inplace=True)
        print(gas_station)
        return gas_station


    def test3(self):
        gas_station = self.test2()
        gas_station.boxplot(column='경유가격', by='셀프')
        plt.show()
        sns.boxplot(x='브랜드', y='경유가격', hue='셀프', data=gas_station)
        plt.show()

    def test4(self):
        gas_station = self.test2()
        print(gas_station.sort_values(by='경유가격', ascending=False).head(10))
        print(gas_station.sort_values(by='경유가격', ascending=True).head(10))

if __name__ == '__main__':
    Oil_Station().test4()
