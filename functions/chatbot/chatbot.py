# -*- coding: utf-8 -*-
import os
import requests

import const
import slack
import dynamodb

def handle(response, context):
  # 카톡에서 보낸 키워드를 API Gateway 응답에서 가져 온 뒤

  # 키워드에 따라 가져올 디비 테이블 결정한 뒤

  # 디비에서 데이터를 가져 와서
  living_life_qt_table = dynamodb.get_living_life_qt_table()
  qt_data = dynamodb.query_qt(living_life_qt_table)

  # 카톡으로 반환할 텍스트를 포매팅한 뒤 반환

  date = qt_data['date']
  text = qt_data['text']

  # API Gateway 에선 람다에서 받은 스트링을 카톡이 원하는 형태의 json 으로 변환해 카톡으로 응답 반환

  message = '%s : %s' % (date, text)
  slack.send_message(os.environ['CHANNEL_ID'], message)
  return { 'status': 200 }

if __name__ == '__main__':
  handle(None, None)
