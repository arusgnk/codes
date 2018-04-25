import Updater
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
import requests
import misc
token = misc.token
updater = Updater(token)
dispatcher = updater.dispatcher

def start_reply(bot, update):
	text = 'Hello! I can convert letters to digits ;)'
	bot.send_message(chat_id=update.message.chat_id, text=text)

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start_reply)
dispatcher.add_handler(start_handler)

def echo_reply(bot, update):
	text = update.message.text.lower()
	
	if text == 'a':
	
		bot.send_message(chat_id=update.message.chat_id, text='0')
	elif text == 'b':	
		bot.send_message(chat_id=update.message.chat_id, text='1')
	else:
		text = 'NO option!'
		bot.send_message(chat_id=update.message.chat_id, text=text)
	

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo_reply)
dispatcher.add_handler(echo_handler)

updater.start_polling()