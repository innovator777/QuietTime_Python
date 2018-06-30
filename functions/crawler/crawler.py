# -*- coding: utf-8 -*-
import os
from time import sleep

import slack
# import dynamodb
# import const
import extract
import env
from selenium import webdriver
from bs4 import BeautifulSoup

def handle(response, context):
  options = webdriver.ChromeOptions()
  options.add_argument("--headless")
  options.add_argument("--disable-gpu")
  options.add_argument("--window-size=1280x1696")
  options.add_argument("--disable-application-cache")
  options.add_argument("--disable-infobars")
  options.add_argument("--no-sandbox")
  options.add_argument("--hide-scrollbars")
  options.add_argument("--enable-logging")
  options.add_argument("--log-level=0")
  options.add_argument("--v=99")
  options.add_argument("--single-process")
  options.add_argument("--ignore-certificate-errors")
  options.add_argument("--homedir=/tmp")
  options.binary_location = "./bin/headless_chromium"

  # driver = webdriver.Chrome("./bin/chromedriver", chrome_options=options)
  # driver.get("https://www.google.co.kr")
  # title = driver.title
  # driver.close()

  driver = webdriver.Chrome("./bin/chromedriver", chrome_options=options)
  driver.implicitly_wait(3)
  driver.get('http://www.duranno.com/qt/default.asp?CAT=020200')
  sleep(3)
  driver.implicitly_wait(3)
  driver.find_element_by_xpath('//*[@id="project_detail"]/div[2]/ul/ul/li[3]/a').click()
  sleep(3)

  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')

  driver.close()

  mainTitle = extract.getMainTitle(soup)

  # 카톡에서 보낸 키워드를 API Gateway 응답에서 가져 온 뒤

  # 키워드에 따라 가져올 디비 테이블 결정한 뒤

  # 디비에서 데이터를 가져 와서

  # 카톡으로 반환할 텍스트를 포매팅한 뒤 반환
  # living_life_qt_table = dynamodb.get_living_life_qt_table()

  # 사이트에 따라 테이블은 구분하고 같은 자료 구조로 삽입
  # dynamodb.insert_qt(living_life_qt_table, mainTitle)

  # API Gateway 에선 람다에서 받은 스트링을 카톡이 원하는 형태의 json 으로 변환해 카톡으로 응답 반환

  # message = "Test Message"
  # kst_now = dynamodb.get_kst_now()
  # date_key = dynamodb.generate_date_key(kst_now)
  slack.send_message(env.getChannelId(), '%s %s' % (mainTitle, u'크롤링 완료'))

  return { 'message':
    { 'text': mainTitle }
  }

if __name__ == '__main__':
  handle(None, None)
