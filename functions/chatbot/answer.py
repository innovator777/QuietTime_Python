#-*- coding:utf-8 -*-

import kw


def getMain():
  return {
    'message': {
      'text': '처음으로'
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getTodaysQTMainTitle()]
    }
  }

def getQTChoice():
  return {
    'message': {
      'text': '항목을 선택해주세요.'
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getLLQTMainTitle(), kw.getDBQTMainTitle(), kw.getHome()]
    }
  }

def getLLQTChoice():
  return {
    'message': {
      'text': '항목을 선택해주세요.'
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getLLQTSubTitle(), kw.getLLQTCommentary(), kw.getHome()]
    }
  }

def getDBQTChoice():
  return {
    'message': {
      'text': '항목을 선택해주세요.'
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getHome()]
    }
  }

def getLLQT(text):
  return {
    'message': {
      'text': text
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getLLQTSubTitle(), kw.getLLQTCommentary(), kw.getHome()]
    }
  }

def getDBQT(text):
  return {
    'message': {
      'text': text
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getLLQTMainTitle(), kw.getDBQTMainTitle(), kw.getHome()]
    }
  }
