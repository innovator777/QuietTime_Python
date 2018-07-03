# -*- coding: utf-8 -*-
import os
import requests
from json import loads, dumps
import re

import const
import slack
import dynamodb
import answer
import kw

def handle(response, context):
  if response:
    content = response['content']
    user_key = response['user_key']

    if content == kw.getTodaysQTMainTitle():
      return answer.getQTChoice()

    elif content == kw.getLLQTMainTitle():
      return answer.getLLQTChoice()

    elif content == kw.getLLQTSubTitle():
      living_life_qt_table = dynamodb.get_living_life_qt_table()
      data = dynamodb.query_living_life_qt(living_life_qt_table)
      return answer.getLLQT(data[const.KEY_LIVING_LIFE_DATA])

    elif content == kw.getLLQTCommentary():
      living_life_qt_table = dynamodb.get_living_life_qt_table()
      data = dynamodb.query_living_life_qt(living_life_qt_table)
      return answer.getLLQT(data[const.KEY_LIVING_LIFE_COMM])

    elif content == kw.getHome():
      return answer.getMain()

    else :
      return answer.getMain()

  return { 'status': 200 }

# if __name__ == '__main__':
#   handle(None, None)
