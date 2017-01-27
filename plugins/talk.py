#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2017-01-27

import requests, json

def docomo_talk(msg):
  url = 'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue'
  apikey = open('plugins/docomo_dialog.token').readline().strip()
  headers = {'content-type': 'application/json'}
  payload = {'APIKEY': apikey}
  data = {
      'utt': msg,
      'nickname': '円谷出',
      'sex': '男',
      'birthdateY': '1990',
      'birthdateM': '4',
      'birthdateD': '1',
      'age': '50',
      'place': '広島',
      't': '30'
  }

  r = requests.post(url, data=json.dumps(data), headers=headers, params=payload)

  reply = r.json()['utt']

  return reply


def docomo_qa(msg):
  url = 'https://api.apigw.smt.docomo.ne.jp/knowledgeQA/v1/ask'
  apikey = open('plugins/docomo_dialog.token').readline().strip()
  headers = {'content-type': 'application/json'}
  payload = {
      'APIKEY': apikey,
      'q': msg
  }
  r = requests.get(url, headers=headers, params=payload)
  reply = r.json()['message']['textForDisplay']

  return reply
