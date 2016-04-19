# -*- coding: utf8 -*-

import sys
import time
import pprint
import telepot
import amis
import re

CONFIG_FILE = 'tgbot.cfg'

def handle(msg):
    db = amis.loaddb()
    num = re.compile(r'[0-9]+')
    try:
        userid = msg['from']['id']
        username = msg['from']['username']
    except:
        print 'Wrong incoming message.'
        pprint.pprint(msg)
        return
    if 'text' in msg and msg['text'] == u'/start':
        print 'sending hello msg to %d' % userid
        bot.sendMessage(userid, u"Nga'ayho %s! 歡迎使用阿美語萌典 BOT" % username)
        return
    if 'text' in msg:
        query = msg['text']
        if num.match(query):
            choice = int(query)
            r = amis.user_input(db, choice, userid)
        else:
            r = amis.lookup(db, query, userid)
        pprint.pprint(amis.USER_LASTWORD)
        bot.sendMessage(userid, r)


if __name__ == '__main__':
    TOKEN = open(CONFIG_FILE).readline().strip()
    bot = telepot.Bot(TOKEN)
    bot.message_loop(handle)
    print 'Listening...'
    while True:
        time.sleep(10)
