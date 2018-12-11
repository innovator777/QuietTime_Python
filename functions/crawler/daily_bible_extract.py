# -*- coding: utf-8 -*-

import re
import env
import slack
import word

def getMainTitle(soup):
  result = list()
  title = soup.select("#bible_text")
  for target in title:
    result.append(target.text)

  return ' '.join(result)

def getPraise(soup):
  result = list()
  praise = soup.select("#bibleinfo_box")
  for target in praise:
    result.append(target.text) 

  return ' '.join(result)

def getAllVerse(soup):
  result = list()
  regex = re.compile(r'(\d+)')
  verse = soup.select("#body_list > li")
  for target in verse:
    data = regex.search(target.text)

    if data:
      length = len(data.group(1))
      number = target.text[:length]
      text = target.text[length:]

    result.append(number + ' ' + text + '\n')

  return ' '.join(result)

def getScripture(soup):
  result = list()
  scripture = soup.select("#body_cont_3 > div")

  for target in scripture:
    result.append(re.sub('[\n]', ' ', target.text))

  return ' '.join(result)

def getExtractVerse(soup):
  verse = getAllVerse(soup)
  regex = re.compile(r'.*?\[(.*)].*')
  data = regex.search(verse)

  if data:
    return data.group(1)
  else:
    return None
