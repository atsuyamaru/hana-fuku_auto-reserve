import json
import time

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# chrome driver manager: バージョンを自動的に合わせる
from webdriver_manager.chrome import ChromeDriverManager
# ChromeとChrome driverを開いたままにさせておく
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 予約ページへアクセス
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://ssc6.doctorqube.com/hana-fuku/")
time.sleep(2)

element = driver.find_element(by="xpath", value="//*[@id='news']/div/div[3]/div[2]/a")
element.click()
time.sleep(2)

element = driver.find_element(by="xpath", value="//*[@id='yoyaku']/div/div[2]/div[1]/a")
element.click()
time.sleep(2)

# フォーム入力
input_name = driver.find_element(by="xpath", value="//*[@id='c_name']")
input_name.click()
input_name.send_keys(personal_info['fullname'])
time.sleep(3)

input_kana = driver.find_element(by="xpath", value="//*[@id='c_kana']")
input_kana.click()
input_kana.send_keys(personal_info['fullname_kana'])
time.sleep(3)

input_tel = driver.find_element(by="xpath", value="//*[@id='c_tel']")
input_tel.click()
input_tel.send_keys(personal_info['phone'])
time.sleep(3)

input_birthdate = driver.find_element(by="xpath", value="//*[@id='c_birth']")
input_birthdate.click()
input_birthdate.send_keys(personal_info['birthday'])
time.sleep(3)

select_sex = driver.find_element(by="xpath", value="//*[@id='c_sex']")
select_sex.click()
select_sex.send_keys(personal_info['sex'])
time.sleep(2)

input_email = driver.find_element(by="xpath", value="//*[@id='c_email']")
input_email.click()
input_email.send_keys(personal_info['email'])
time.sleep(3)

ok_button = driver.find_element(by="xpath", value="//*[@id='yoyaku']/div/div[2]/form/input[5]")
ok_button.click()

go_reserve_btn = driver.find_element(by="xpath", value="//*[@id='yoyaku']/div/div[2]/ul/div/li/a")
time.sleep(2)
go_reserve_btn.click()

first_time_reserve_btn = driver.find_element(by="xpath", value="//*[@id='yoyaku']/div/div[2]/ul/div/li/a")
time.sleep(2)
first_time_reserve_btn.click()



