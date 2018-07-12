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
      user_table = dynamodb.get_user_table()
      user_data = dynamodb.query_target_user(user_table, user_key)

      if user_data :
        if const.KEY_USER_ADMIN in user_data:
          admin = user_data[const.KEY_USER_ADMIN]
          if admin == 'TRUE':
            return answer.getAdmin()

        admission = user_data[const.KEY_USER_ADMISSION]
        if admission == 'TRUE':
          return answer.getQTChoice()
        else:
          return answer.getDisapprovedUserCase()
      else:
        return answer.getUnappliedUserCase()

    elif content == kw.getAdminFunction():
      return answer.getAdminMode()

    elif content == kw.getLLQTMainTitle():
      return answer.getLLQTChoice()

    elif content == kw.getLLQTSubTitle():
      living_life_qt_table = dynamodb.get_living_life_qt_table()
      data = dynamodb.query_living_life_qt(living_life_qt_table)
      if data is None:
        return answer.getLLQT(data)
      else:
        return answer.getLLQT(data[const.KEY_LIVING_LIFE_DATA])

    elif content == kw.getLLQTCommentary():
      living_life_qt_table = dynamodb.get_living_life_qt_table()
      data = dynamodb.query_living_life_qt(living_life_qt_table)
      if data is None:
        return answer.getLLQT(data)
      else:
        return answer.getLLQT(data[const.KEY_LIVING_LIFE_COMM])

    elif content == kw.getDBQTMainTitle():
      daily_bible_qt_table = dynamodb.get_daily_bible_qt_table()
      data = dynamodb.query_daily_bible_qt(daily_bible_qt_table)
      if data is None:
        return answer.getDBQT(data)
      else:
        return answer.getDBQT(data[const.KEY_DAILY_BIBLE_DATA])

    elif content == kw.getHome():
      return answer.getMain()

    elif content == kw.getApply():
      return answer.getApplyManual()

    elif content == kw.getChangeUserState():
      return answer.getUserStateChangeMode()

    elif content == kw.getWaitList():
      user_table = dynamodb.get_user_table()
      waitList = dynamodb.query_wait_user(user_table)
      if waitList is not None:
        userList = list()
        for target in waitList:
          userList.append(target[const.KEY_USER_KEY] + ' : ' + target[const.KEY_USER_INFO] + '\n')
        waitString = '\n'.join(userList)
        return answer.getWaitUserList(waitString)
      else:
        return answer.getWaitUserList(None)
    elif content == kw.getApproveList():
      user_table = dynamodb.get_user_table()
      approveList = dynamodb.query_approve_user(user_table)
      if approveList is not None:
        userList = list()
        for target in approveList:
          userList.append(target[const.KEY_USER_KEY] + ' : ' + target[const.KEY_USER_INFO] + '\n')
        approveString = '\n'.join(userList)
        return answer.getApproveUserList(approveString)
      else:
        return answer.getApproveUserList(None)
    else :
      user_table = dynamodb.get_user_table()
      user_data = dynamodb.query_target_user(user_table, user_key)

      if user_data :
        if const.KEY_USER_ADMIN in user_data:
          admin = user_data[const.KEY_USER_ADMIN]
          if admin == 'TRUE':
            target_user_data = dynamodb.query_target_user(user_table, content)
            if target_user_data:
              admission = user_data[const.KEY_USER_ADMISSION]
              if admission == 'FALSE':
                dynamodb.update_user(user_table, content, 'TRUE')
                return answer.getMain()
              else:
                dynamodb.update_user(user_table, content, 'FALSE')
                return answer.getMain()
            else:
              return answer.getEnterIncorrectlyWord()
        else:
          return answer.getWrongAccess()
      else:
        dynamodb.insert_user(user_table, user_key, content)
        slack.send_message(os.environ['CHANNEL_ID'], '%s : %s' % (user_key, content))
        return answer.getApplyQuietTime()


  return { 'status': 200 }

# if __name__ == '__main__':
#   handle(None, None)
