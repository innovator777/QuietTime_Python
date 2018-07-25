# -*- coding: utf-8 -*-
import os
from time import sleep

import slack
import dynamodb
import living_life_extract
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
  driver.get(env.getLivingLifePath())
  sleep(3)
  driver.implicitly_wait(3)
  driver.find_element_by_xpath('//*[@id="project_detail"]/div[2]/ul/ul/li[3]/a').click()
  sleep(3)

  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')

  driver.close()

  todaysWord = getTodaysWord(soup)
  todaysCommentary = getTodaysCommentary(soup)

  living_life_qt_table = dynamodb.get_living_life_qt_table()

  dynamodb.insert_living_life_qt(living_life_qt_table, todaysWord, todaysCommentary)

  slack.send_message(env.getChannelId(), '%s' % (todaysWord))
  slack.send_message(env.getChannelId(), '%s' % (todaysCommentary))

  return { 'status': 200 }

def getTodaysWord(soup):
  mainTitle = living_life_extract.getMainTitle(soup)
  allVerse = living_life_extract.getAllVerse(soup)
  praise = living_life_extract.getPraise(soup)
  helper = living_life_extract.getHelper(soup)
  mainText = ' '.join(living_life_extract.getMainText(soup)) # list to string

  return mainTitle + '\n' + allVerse + '\n' + praise + '\n' + mainText + '\n' + helper

def getTodaysCommentary(soup):
  mainTitle = living_life_extract.getMainTitle(soup)
  allVerse = living_life_extract.getAllVerse(soup)
  summary = living_life_extract.getSummary(soup)
  commentary = ' '.join(living_life_extract.getCommentary(soup)) #list to string
  prayer = living_life_extract.getPrayer(soup)

  return mainTitle + '\n' + allVerse + '\n' + summary + '\n' + commentary + prayer

if __name__ == '__main__':
  handle(None, None)
