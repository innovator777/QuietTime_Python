# -*- coding: utf-8 -*-
import os

import slack
import dynamodb
import const

def handle(response, context):
  # 카톡에서 보낸 키워드를 API Gateway 응답에서 가져 온 뒤

  # 키워드에 따라 가져올 디비 테이블 결정한 뒤

  # 디비에서 데이터를 가져 와서

  # 카톡으로 반환할 텍스트를 포매팅한 뒤 반환
  living_life_qt_table = dynamodb.get_living_life_qt_table()

  # 사이트에 따라 테이블은 구분하고 같은 자료 구조로 삽입
  dynamodb.insert_qt(living_life_qt_table, 'Text')

  # API Gateway 에선 람다에서 받은 스트링을 카톡이 원하는 형태의 json 으로 변환해 카톡으로 응답 반환

  # message = "Test Message"
  kst_now = dynamodb.get_kst_now()
  date_key = dynamodb.generate_date_key(kst_now)
  slack.send_message(os.environ['CHANNEL_ID'], '%s %s' % (date_key, u'데이터 저장 완료'))

  return { 'status': 200 }

if __name__ == '__main__':
  handle(None, None)
