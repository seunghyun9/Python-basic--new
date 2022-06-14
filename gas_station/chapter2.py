from selenium import webdriver
# 2 서울시 구별 주유소 가격 정보 얻기
driver = webdriver.Chrome('C:/Users/seunghyun/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("http://www.opinet.co.kr/searRgSelect.do")
gu_list_raw = driver.find_element_by_xpath("""//*[@id="SIGUNGU_NM0"]""")
gu_list = gu_list_raw.find_elements_by_tag_name("option")
gu_names = [option.get_attribute("value") for option in gu_list]
gu_names.remove('')
print(gu_names)