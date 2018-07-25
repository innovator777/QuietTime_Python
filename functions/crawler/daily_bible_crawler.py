# -*- coding: utf-8 -*-
import os
from time import sleep

import slack
import dynamodb
# import const
import daily_bible_extract
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

  driver = webdriver.Chrome("./bin/chromedriver", chrome_options=options)
  driver.implicitly_wait(3)
  driver.get(env.getDailyBiblePath())
  sleep(3)

  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')

  driver.close()

  todaysQuietTime = getTodaysQuiteTime(soup)

  daily_bible_qt_table = dynamodb.get_daily_bible_qt_table()
  dynamodb.insert_daily_bible_qt(daily_bible_qt_table, todaysQuietTime)

  slack.send_message(env.getChannelId(), '%s' % (todaysQuietTime))

  return { 'status': 200 }

def getTodaysQuiteTime(soup):
  mainTitle = daily_bible_extract.getMainTitle(soup)
  praise = daily_bible_extract.getPraise(soup)
  verse = daily_bible_extract.getExtractVerse(soup)
  scripture = daily_bible_extract.getScripture(soup)
  commentary = daily_bible_extract.getCommentary(soup)
  commentaryText = daily_bible_extract.getCommentaryText(soup)

  return mainTitle + '\n\n' + praise + '\n\n' + verse + '\n\n' + scripture + '\n\n' + commentary + '\n\n' + commentaryText


if __name__ == '__main__':
  handle(None, None)
