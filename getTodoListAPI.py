#!/bin/env python

import requests

resp = requests.get('https://todolist.example.com/tasks/')

# check for problems
if resp.status_code != 200:
   #This means something went wrong
   raise ApiError('Get /tasks/ {}'.format(resp.status_code))

# no problems?
for todo_item in resp.json():
   print('{} {}'.format(todo_item['id'], todo_item['summary']))
