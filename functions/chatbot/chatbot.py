import os
import requests

import slack

def handle(response, context):
  message = "Test Message"
  slack.send_message(os.environ['CHANNEL_ID'], message)
  return { 'status': 200 }

if __name__ == '__main__':
  handle(None, None)
