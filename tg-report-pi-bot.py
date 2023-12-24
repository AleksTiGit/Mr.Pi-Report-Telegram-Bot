import telebot

bot = telebot.TeleBot('token')

report_list = []

@bot.message_handler(commands=['report'])
def report(message):
  if message.reply_to_message:
    report_message_id = message.message_id
    message_text_report = 'Репорт отправлен'
    bot.reply_to(message,message_text_report,parse_mode='Markdown')
    report_list.append(f'Репорт https://t.me/c/chat_id/{report_message_id}')

@bot.message_handler(commands=['report_list'])
def func_report_list(message):
  bot.send_message(message.chat.id, f'{report_list}' , parse_mode= 'Markdown')

bot.polling(non_stop=True)