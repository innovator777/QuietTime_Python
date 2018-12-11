# -*- coding: utf-8 -*-
import os
from time import sleep

import slack
import dynamodb
import daily_bible_extract
import env
from selenium import webdriver
from bs4 import BeautifulSoup

def handle(response, context):
  todaysQuietTime = getTodaysQuiteTime(getSoup(env.getDailyBiblePath()))
  todaysQuietTimeSoon = getTodaysQuiteTime(getSoup(env.getDailyBiblePath(), 'soon'))

  daily_bible_qt_table = dynamodb.get_daily_bible_qt_table()
  dynamodb.insert_daily_bible_qt(daily_bible_qt_table, todaysQuietTime, todaysQuietTimeSoon)

  slack.send_message(env.getChannelId(), '%s' % (todaysQuietTime))
  slack.send_message(env.getChannelId(), '%s' % (todaysQuietTimeSoon))

  return { 'status': 200 }

def getSoup(path, type='basic'):
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

  driver = webdriver.Chrome("./bin/chromedriver", chrome_options=options)
  driver.implicitly_wait(3)
  driver.get(path)
  sleep(3)
  driver.implicitly_wait(3)

  if type == 'soon':
    driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/ul/li[2]/div[1]').click()
    sleep(3)
    driver.implicitly_wait(3)

  driver.find_element_by_xpath('//*[@id="mainTitle_3"]').click()
  sleep(3)
  driver.implicitly_wait(3)

  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')

  driver.close()

  return soup

def getTodaysQuiteTime(soup):
  mainTitle = daily_bible_extract.getMainTitle(soup)
  praise = daily_bible_extract.getPraise(soup)
  verse = daily_bible_extract.getAllVerse(soup)
  scripture = daily_bible_extract.getScripture(soup)

  return mainTitle + '\n\n' + praise + '\n\n' + verse + '\n\n' + '해설 : ' + scripture


if __name__ == '__main__':
  handle(None, None)
