import boto3 # DB
from boto3.dynamodb.conditions import Key, Attr
import datetime
from pytz import timezone
from decimal import *

import const

def get_db():
  return boto3.resource('dynamodb')

#living_life_qt
def get_living_life_qt_table():
  dynamodb = get_db()
  return dynamodb.Table('Living_Life_QT_Table')

def insert_living_life_qt(table, data, commentary):
  kst_now = get_kst_now()
  date_key = generate_date_key(kst_now)

  table.put_item(Item={
    const.KEY_DATE: date_key,
    const.KEY_LIVING_LIFE_DATA: data,
    const.KEY_LIVING_LIFE_COMM: commentary
  })

def query_living_life_qt(table):
  kst_now = get_kst_now()
  date_key = generate_date_key(kst_now)
  filter_exp = Key(const.KEY_DATE).eq(date_key)
  response = table.scan(FilterExpression=filter_exp)
  return response['Items'][0]

#daily_bible_qt
def get_daily_bible_qt_table():
  dynamodb = get_db()
  return dynamodb.Table('Daily_Bible_QT_Table')

def insert_daily_bible_qt(table, data, soon):
  kst_now = get_kst_now()
  date_key = generate_date_key(kst_now)

  table.put_item(Item={
    const.KEY_DATE: date_key,
    const.KEY_DAILY_BIBLE_DATA: data,
    const.KEY_DAILY_BIBLE_SOON: soon,
  })

def query_daily_bible_qt(table):
  kst_now = get_kst_now()
  date_key = generate_date_key(kst_now)
  filter_exp = Key(const.KEY_DATE).eq(date_key)
  response = table.scan(FilterExpression=filter_exp)
  if response['Items'] is None or not response['Items']:
    return None
  else:
    return response['Items'][0]


# user_table
def get_user_table():
  dynamodb = get_db()
  return dynamodb.Table('User_Table')

def insert_user(table, user_key, user_info):
  table.put_item(Item={
    const.KEY_USER_KEY: user_key,
    const.KEY_USER_INFO: user_info,
    const.KEY_USER_ADMISSION: 'FALSE'
  })

def query_target_user(table, user_key):
  filter_exp = Key(const.KEY_USER_KEY).eq(user_key)
  response = table.scan(FilterExpression=filter_exp)
  if response['Items'] is None or not response['Items']:
    return None
  else :
    return response['Items'][0]

def query_wait_user(table):
  filter_exp = Attr(const.KEY_USER_ADMISSION).eq('FALSE')
  response = table.scan(FilterExpression=filter_exp)
  if response['Items'] is None or not response['Items']:
    return None
  else :
    return response['Items']

def query_approve_user(table):
  filter_exp = Attr(const.KEY_USER_ADMISSION).eq('TRUE')
  response = table.scan(FilterExpression=filter_exp)
  if response['Items'] is None or not response['Items']:
    return None
  else :
    return response['Items']


def update_user(table, user_key, user_admission):
  table.update_item(
    Key={
        const.KEY_USER_KEY: user_key,
    },
    UpdateExpression='SET user_admission = :val',
    ExpressionAttributeValues={
        ':val': user_admission
    })



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
