import boto3 # DB
from boto3.dynamodb.conditions import Key, Attr
import datetime
from pytz import timezone
from decimal import *

import const

def get_db():
  return boto3.resource('dynamodb')

def get_living_life_qt_table():
  dynamodb = get_db()
  return dynamodb.Table('Living_Life_QT_Table')

def insert_qt(table, text):
  kst_now = get_kst_now()
  date_key = generate_date_key(kst_now)

  table.put_item(Item={
    const.KEY_DATE: date_key,
    'text': text,
  })

def query_qt(table):
  kst_now = get_kst_now()
  date_key = generate_date_key(kst_now)
  filter_exp = Key(const.KEY_DATE).eq(date_key)
  response = table.scan(FilterExpression=filter_exp)
  return response['Items'][0]

# Date
def get_kst_now():
  return datetime.datetime.now(timezone('Asia/Seoul'))

def generate_date_key(kst_now):
  month_str = '%s' % kst_now.month
  if kst_now.month < 10:
    month_str = '0' + month_str

  day_str = '%s' % kst_now.day
  if kst_now.day < 10:
    day_str = '0' + day_str

  return '%s%s%s' % (kst_now.year, month_str, day_str)
