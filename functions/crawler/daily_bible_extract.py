# -*- coding: utf-8 -*-

import re
import env
import slack
import word

def getMainTitle(soup):
  result = list()
  title = soup.select("#searchVO > ul.story_view > li > p.subject")
  for target in title:
    result.append(target.text)

  return ' '.join(result)

def getPraise(soup):
  result = list()
  praise = soup.select("#searchVO > ul.story_view > li > p.book_num > a")
  for target in praise:
    result.append(target.text)

  return ' '.join(result)

def getAllVerse(soup):
  result = list()
  verse = soup.select("#searchVO > ul.story_view > li > p.book_line")
  for target in verse:
    result.append(target.text)

  return ' '.join(result)

def getScripture(soup):
  result = list()
  scripture = soup.select("#searchVO > ul.story_view > li > table")

  for target in scripture:
    result.append(target.text.rstrip())

  return ' '.join(result)

def getCommentary(soup):
  result = list()
  commentary = soup.select("#searchVO > ul.story_view > li > p.book_line2")
  result.append(word.getCommentary())
  for target in commentary:
    result.append(re.sub(' +', ' ', target.text).strip())

  return ' '.join(result)

def getCommentaryText(soup):
  result = list()
  commentaryText = soup.select("#bibleTxt")
  for target in commentaryText:
    result.append(re.sub(' +', ' ', target.text).strip())

  return ' '.join(result)

def getExtractVerse(soup):
  verse = getAllVerse(soup)
  regex = re.compile(r'.*?\[(.*)].*')
  data = regex.search(verse)

  if data:
    return data.group(1)
  else:
    return None
