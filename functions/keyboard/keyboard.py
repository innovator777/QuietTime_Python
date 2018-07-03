# -*- coding: utf-8 -*-

def handle(response, context):
  return {
    'type': 'buttons',
    'buttons': ['오늘의 큐티']
  }

  # return {
  #   "type": "text"
  # }

if __name__ == '__main__':
  handle(None, None)
