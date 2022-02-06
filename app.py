import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import random
import time
from datetime import datetime
client = WebClient(token="xoxp-2288835779184-2250422671751-2265541997522-4107a2540f1a18ca9fd3d5f4bf45e07f")

def sendMsg(msg, chn):
  try:
      response = client.chat_postMessage(channel=chn, text=msg)
      assert response["message"]["text"] == msg
  except SlackApiError as e:
      # You will get a SlackApiError if "ok" is False
      assert e.response["ok"] is False
      assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
      print(f"Got an error: {e.response['error']}")

tasks = ['LeetCode', 'Chinese Worksheet']
times = ['1hr','30min']

# tasks = ['Data Structures', 'Chinese Reading', 'LeetCode', 'Write Economist', 'Chinese Worksheet', 'English Reading', 'Math(Khan)']
# times = ['1hr','30min','1hr','30min','1hr','30min','30min']
####|Dont forget to delte project after usage
####|
####|
####|
####|


current_time = ""

now = datetime.now()
current_time = now.strftime("%H:%M")


def doTask():
  taskN = random.randint(0, len(tasks)-1)
  waitTime = 0
  if times[taskN] == '1hr':
    waitTime = 60*60
  if times[taskN] == '30min':
    waitTime = 60*30
  msgS = f"<@U027TAC97KM>, <@U027CCEKRN3> is Starting Project {tasks[taskN]} for {times[taskN]}, Adding to Tracking....."
  print("Sent to to Tracking")
  sendMsg(msgS, "#notifications")
  now = datetime.now()
  current_time = now.strftime("%H:%M")
  sendMsg(f"Starting Project {tasks[taskN]} for {times[taskN]} at {current_time}", "#tracking")
  for i in range(waitTime):
    time.sleep(1)
    print(i)
  print("Project Marked as Finished")
  sendMsg(f"Hey, <@U027CCEKRN3>, time's up, <@U027TAC97KM>, Marking Project as Finished", "#notifactions")
  now = datetime.now()
  current_time = now.strftime("%H:%M")
  sendMsg(f"Project {tasks[taskN]} finished in {times[taskN]} at {current_time}", "#tracking")
  sendMsg("---------------------------------------------------------------------- \n ‎‎", "#tracking")
  del tasks[taskN]
  del times[taskN]

doTask()

