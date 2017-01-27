#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2017-01-27

import re
from slackbot.bot import respond_to, listen_to, default_reply
from plugins.weather import get_rainfall
from plugins.talk import docomo_talk, docomo_qa

@respond_to('疲れた')
@respond_to('つかれた')
def cheer(message):
  message.reply('ファイト!')


@listen_to('すまん')
@listen_to('すまない')
@listen_to('すまぬ')
@listen_to('ごめん')
@listen_to('申し訳')
@listen_to('SUMANU')
@respond_to('すまん')
@respond_to('すまない')
@respond_to('すまぬ')
@respond_to('ごめん')
@respond_to('申し訳')
def eenyade(message):
  message.reply('ええんやで（ﾆｯｺﾘ')


@respond_to('天気')
def get_weather(message):
  rainfall_now = get_rainfall()
  msg = 'ただいまの降水量は %d mm/h です' % int(rainfall_now)
  message.reply(msg)

@listen_to('あきらめたら')
@listen_to('諦めたら')
def anzai(message):
  message.send('そこで試合終了ですよ。')

@listen_to('いいですか')
def reaction(message):
  message.react('+1')

@listen_to('いいですね！')
def reaction2(message):
  message.react('+1')

@respond_to('::debug')
def debug(message):
  t = dir(str(message))
  message.send(t)

@respond_to('.*は[\?？]$', re.IGNORECASE)
def qa(message):
  msg = docomo_qa(message.body['text'])
  message.reply(msg)

@default_reply
def my_default_hanlder(message):
  msg = docomo_talk(message.body['text'])
  message.reply(msg)
