# from telegram import (KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton)
# from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
#                           ConversationHandler)
# import logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)
# import misc
# token = misc.token
# CODING, CONVERTNG_TEXT, TRANSLATING_TEXT = range(3)

# def start(bot, update):
#     reply_keyboard = [['Converting', 'Translating']]
#     update.messsage.reply_text(
#         'Hello! I can convert letters in old kazakh alphabet to the letters in new alphabet. Also you can translate words in russian :)\n'
#         'Choose Converting or Translating!',
#         reply_keyboard=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
#     return CODING

# def coding(bot, update):
#     text = update.message.text
#     if text == 'Converting':
#         bot.send_message(chat_id=update.message.chat_id, text="I am ready:)")
#     return CONVERTNG_TEXT          
# def converting_text(bot, update):
#     text = update.message.text.lower()
#     if "a" in text:
#         bot.send_message(chat_id=update.message.chat_id, text='1') 
#     elif "b" in text:
#         bot.send_message(chat_id=update.message.chat_id, text='2')     
#     elif "c" in text:
#         bot.send_message(chat_id=update.message.chat_id, text='3')  
           
#     # elif "в" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='v')
#     # elif "г" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='g')     
#     # elif "ғ" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='ǵ')     
#     # elif "д" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='d')     
#     # elif "ж" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='j')     
#     # elif "з" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='z')                  
#     # elif "и" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='i')     
#     # elif "й" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='i')     
#     # elif "к" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='k')     
#     # elif "қ" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='q')     
#     # elif "л" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='l')     
#     # elif "м" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='m')     
#     # elif "н" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='n')     
#     # elif "ң" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='ń')     
#     # elif "о" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='o')
#     # elif "ө" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='ó')      
#     # elif "п" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='p')
#     # elif "р" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='r')
#     # elif "с" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='s')
#     # elif "т" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='t')
#     # elif "у" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='ý')
#     # elif "ұ" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='u')
#     # elif "ү" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='ú')
#     # elif "ф" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='f')                                  
#     # elif "х" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='h')
#     # elif "һ" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='h')
#     # elif "ц" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='-')
#     # elif "ч" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='ch')
#     # elif "ш" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='sh')
#     # elif "щ" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='-')           
#     # elif "ъ" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='-')
#     # elif "ы" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='y')
#     # elif "і" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='i')
#     # elif "ь" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='-')
#     # elif "э" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='-')
#     # elif "ю" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='-')
#     # elif "я" in text:
#     #     bot.send_message(chat_id=update.message.chat_id, text='-')
#     else:
#         bot.send_message(chat_id=update.message.chat_id, text='Please, try again...')
#         return ConversationHandler.END 
#         text = update.message.text
#         if text == 'Translating':
#             bot.send_message(chat_id=update.message.chat_id, text="Okay, let's translate!")
#             return TRANSLATING_TEXT
#             def translating_text(bot, update):
#                 text = update.message.text.lower()
#                 from bs4 import BeautifulSoup
#                 url = 'https://sozdik.kz/translate/ru/kk/%s/' % text
#                 r = requests.get(url)
#                 data = r.json()
#                 translation = data['translation']
#                 from bs4 import BeautifulSoup
#                 soup = BeautifulSoup(translation, 'html.parser')
#                 text = soup.select('a')[0].text
#                 text = translated_text
#             bot.send_message(chat_id=update.message.chat_id, text="translated_text")    
#         return ConversationHandler.END  

#  def cancel(bot, update):
#     user = update.message.from_user
#     logger.info("User %s canceled the conversation.", user.first_name, update.message.text)
#     update.message.reply_text('Bye!',
#                               reply_markup=ReplyKeyboardRemove())

#     return ConversationHandler.END


# def error(bot, update, error):
#     """Log Errors caused by Updates."""
#     logger.warning('Update "%s" caused error "%s"', update, error)

             
        
    
# # def build_menu(buttons,
# #                n_cols,
# #                header_buttons=None,
# #                footer_buttons=None):
# #     menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
# #     if header_buttons:
# #         menu.insert(0, header_buttons)
# #     if footer_buttons:
# #         menu.append(footer_buttons)
# #     return menu

# # import logging

# # # Enable logging
# # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
# #                     level=logging.INFO)

# # logger = logging.getLogger(__name__)

# # def start(bot, update):
# #     update.message.reply_text(
# #         update.message.text,
# #         reply_markup=ReplyKeyboardRemove())

# def main():
#     updater = Updater(token)
#     dp = updater.dispatcher
#     conv_handler = CommandHandler(
#         entry_points=[CommandHandler('start', start)],

#          states={
#                 CODING: [RegexHandler('^(Converting|Translating)$'), coding)],

#                 CONVERTING_TEXT: [MessageHandler(Filters.text, converting_text)],

#                 TRANSLATING_TEXT: [MessageHandler(Filters.text, translating_text )]
#             },
#          fallbacks=[CommandHandler('cancel', cancel)]
#     )

#     dp.add_handler(conv_handler)
#     dp.add_error_handler(error)
#     updater.start_polling()
#     updater.idle()
# if __name__ == '__main__':
#     main()