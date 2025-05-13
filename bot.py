import telebot

# Твой токен и чат ID
TOKEN = '7534952852:AAE7Fl7yNjV7BFFzZmWawhsw19sUOvkFtkQ'
CHAT_ID = '6962837084'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот и работаю на сервере Render.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(CHAT_ID, f"Ты написал: {message.text}")

bot.polling()
