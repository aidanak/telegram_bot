# -*- coding: utf-8 -*-
import requests
import random
from sys import exit


class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def send_image(self, chat_id, image):
        params = {'chat_id': chat_id, 'photo': image}
        method = 'sendPhoto'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

teacher_bot = BotHandler(u'533306043:AAFjJNSAJLtBhaQPsP1tGkIou5y09PkPf5g')  
sattar = [u'задница', u'сволочь', u'даровская крыса', u'какашка', u'старая каманча', u'упырь', u'гондон', u'пидр', u'дерьмо', u'Жопа с глазками',
          u'Дурак дураком и уши холодные', u'позитивчик', u'сволочь']


def main():
    new_offset = None

    while True:
            try:
                teacher_bot.get_updates(new_offset)

                last_update = teacher_bot.get_last_update()

                last_update_id = last_update['update_id']
                last_chat_text = (last_update['message']['text']).split(' ')
                last_chat_id = last_update['message']['chat']['id']
                if 'first_name' in last_update['message']['from']:
                    if last_update['message']['from']['first_name'] == u'Galima' or last_update['message']['from']['first_name'] == u'Zhanar':
                        teacher_bot.send_image(last_chat_id, u'https://cdn5.imgbb.ru/user/106/1068569/201510/5619bd7852e0a150250c53077740299f.png')
                last_chat_text = [x.lower() for x in last_chat_text]
                if u'попка' in last_chat_text:
                    teacher_bot.send_image(last_chat_id, u'http://www.kbtu.kz/Content/Kbtu/images/teachers/176.jpg')
                if u'саттар' in last_chat_text:
                    teacher_bot.send_message(last_chat_id, random.choice(sattar))
                if u'муслим' in last_chat_text:
                    teacher_bot.send_image(last_chat_id, u'https://cs9.pikabu.ru/post_img/2018/01/14/6/1515920548157545263.png')
                if u'темирулан' in last_chat_text:
                    teacher_bot.send_message(last_chat_id, random.choice(sattar))
                if u'аслан' in last_chat_text:
                    teacher_bot.send_message(last_chat_id, "ненавижу всяких Асланов")

                new_offset = last_update_id + 1
            except Exception as e:
                print str(e)

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
