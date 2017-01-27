#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2017-01-27

import requests

def get_rainfall():
  url = 'https://map.yahooapis.jp/weather/V1/place'
  appid = open('plugins/yolo_weather.token').readline().strip()
  place = '139.732293,35.663613'
  output = 'json'
  payload = {
      'appid': appid,
      'coordinates': place,
      'output': output
  }

  res = requests.get(url, params=payload)
  rainfall_now = res.json()['Feature'][0]['Property']['WeatherList']['Weather'][0]['Rainfall']
  
  return rainfall_now
