import telebot
from datetime import datetime, date

TOKEN = 'your_token'
bot = telebot.TeleBot(TOKEN)

target_date = date(2023, 12, 21)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi, I'm a reporting bot!")

@bot.message_handler(commands=['remained'])
def otchet(message):
    current_date = datetime.now().date()
    current_time = datetime.now().time()
    target_datetime = datetime.combine(target_date, datetime.min.time())
    time_left = target_datetime - datetime.combine(current_date, current_time)
    
    if time_left.total_seconds() < 0:
        bot.send_message(message.chat.id, "The report has expired!")
    else:
        days_left = time_left.days
        hours_left = time_left.seconds // 3600
        minutes_left = (time_left.seconds % 3600) // 60
        seconds_left = time_left.seconds % 60
        
        time_left_str = f"{days_left} Days, {hours_left} hours, {minutes_left} minutes, {seconds_left} seconds"
        
        bot.send_message(message.chat.id, f"before {target_date} remained {time_left_str}")

bot.polling()
