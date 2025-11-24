# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:08:28 2024

@author: HP
"""

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

class TelegramBot:
    def __init__(self, token, controller):
        self.updater = Updater(token)
        self.controller = controller

    def start(self, update: Update, context: CallbackContext):
        update.message.reply_text('Hello! Send /add <value> to add data.')

    def add_data(self, update: Update, context: CallbackContext):
        try:
            value = context.args[0]
            self.controller.add_data(value)
            update.message.reply_text(f'Data added: {value}')
        except IndexError:
            update.message.reply_text('Please provide a value.')

    def run(self):
        dispatcher = self.updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", self.start))
        dispatcher.add_handler(CommandHandler("add", self.add_data))
        self.updater.start_polling()
        self.updater.idle()
