import telebot

bot = telebot.TeleBot('token')

report_list = ['Репорты:']

@bot.message_handler(commands=['report'])
def report(message):
    report_message_id = message.message_id
    message_text_report = 'Репорт отправлен'
    bot.reply_to(message,message_text_report,parse_mode='Markdown')
    report_list.append(f'Репорт https://t.me/c/chat-id/{report_message_id}')

@bot.message_handler(commands=['report_list'])
def func_report_list(message):
  bot.send_message(message.chat.id, f'{report_list}' , parse_mode= 'Markdown')

@bot.message_handler(commands=['report_del'])
def report_del(message):
    report_list.pop(1)
    message_text_del = f'Первый репорт удалён; репорт лист:{report_list}'
    bot.send_message(message.chat.id, message_text_del , parse_mode = 'Markdown')

bot.polling(non_stop=True)
