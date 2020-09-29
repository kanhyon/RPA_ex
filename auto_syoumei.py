# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.alert import Alert
import datetime
import schedule

number = input('学籍番号を入力してください')
pas= input('パスワードを入力してください')
file = input('ファイルのディレクトリを指定してください')

def job():
    # ブラウザを開く
    DRIVER_PATH = '/Users/kanhyon/chromedriver'
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    # CoursePowerの画面を開く
    driver.get("https://study.ns.kogakuin.ac.jp/lms/lginLgir/;SID=s174d65cb830698d6fa75a44d231#")
    # ログインIDを入力
    login_id = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[1]/div[1]/div[2]/input')
    login_id.send_keys(number)
    # パスワードを入力
    password = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[1]/div[2]/div[2]/input')
    password.send_keys(pas)
    # ログインボタンをクリックする
    login_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/button')
    login_btn.click()
    #照明・表示システムをクリックする
    light_btn= driver.find_element_by_xpath('//*[@id="homeHomlForm"]/div[4]/div[4]/div[2]/div[4]/div[2]/div[1]/a')
    light_btn.click()
    #授業を開く
    open_zyugyou_btn= driver.find_element_by_xpath('//*[@id="cs_rightTabinVox"]/div/table/tbody/tr[2]/td[1]')
    open_zyugyou_btn.click()
    #レポート提出画面を開く
    submit_open_btn= driver.find_element_by_xpath('//*[@id="REP0000000263821"]/a')
    submit_open_btn.click()
    #ファイルを添付する
    driver.find_element_by_xpath('//*[@id="makeFile0"]/input').send_keys(file)
    #提出する
    submit_btn= driver.find_element_by_xpath('//*[@id="cs_fullHeadTitle"]/div[1]/div/a')
    submit_btn.click()
    Alert(driver).accept()
    # 10秒待機
    time.sleep(10)
    # ブラウザを終了する。
    driver.close()

schedule.every().day.at("16:00").do(job)

while True:
  schedule.run_pending()
  time.sleep(60)
