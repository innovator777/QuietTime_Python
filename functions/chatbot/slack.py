import requests

# Constants
SLACK_HOOK_URL = 'https://hooks.slack.com/services/'

def send_message(chanel_id, message):
  requests.post(
    SLACK_HOOK_URL + chanel_id,
    headers={'Content-Type': 'application/json'},
    json={'text': message}
  )
