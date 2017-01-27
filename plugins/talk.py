#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2017-01-27

import requests, json

def docomo_talk(msg):
  url = 'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue'
  apikey = '4e3768416a4d782f3330556e4269634c3145427a46726b735a75416767546e48647058754150306b6e4244'
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
