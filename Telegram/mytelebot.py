# -*- coding:utf-8 -*-
import telegram


class NotChatIdError:
    pass


class MyTelegramBot:
    def __init__(self, token, chat=None):
        self.bot = telegram.Bot(token=token)
        self.chat_id = chat

    def set_chat(self, chat):
        self.chat_id = chat

    def set_bot(self, token):
        self.bot = telegram.Bot(token=token)

    def send_message(self, msg_list):
        if not self.chat_id:
            raise NotChatIdError

        for msg in msg_list:
            try:
                if len(msg) <= 3000:
                    self.bot.sendMessage(chat_id=self.chat_id, text=msg, timeout=20)
                else:
                    self.bot.sendMessage(chat_id=self.chat_id, text=msg[:3000], timeout=20)
                    self.bot.sendMessage(chat_id=self.chat_id, text=msg[3000:], timeout=20)
            except telegram.error.TimedOut:
                pass
